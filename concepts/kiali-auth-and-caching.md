---
title: Kiali Authentication
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, security, api]
sources:
  - raw/articles/kiali-doc-auth-and-security.md
  - raw/articles/kiali-repo-cache.md
  - raw/articles/kiali-kep-multi-session-auth.md
  - raw/articles/kiali-kep-graph-cache.md
  - raw/articles/kiali-doc-STATUS.md
---

# Kiali Authentication

How Kiali authenticates users: five strategies, client-side encrypted-cookie sessions, TLS policy,
and credential/CA rotation. Source: `docs/agents /auth-and-security.md` (reviewed
`PASS_WITH_ANNOTATIONS`, 2026-05-26 scribe run). The caching half of this former combined page now
lives in [[kiali-caching]]. Claims dated 2026-09-17. ^[raw/articles/kiali-doc-STATUS.md]

## Overview & the AuthController interface

`handlers/authentication/` holds one controller per strategy; at startup a single `AuthController`
is built from `auth.strategy` and drives the whole session lifecycle (login, per-request
validation, logout):

```go
type AuthController interface {
    Authenticate(r, w) (*UserSessionData, error)   // login; failure -> 401/403
    ValidateSession(r, w) (UserSessions, error)    // every authenticated request
    TerminateSession(r, w) error                   // logout, unconditional
}
```

`UserSessionData` carries `api.AuthInfo` (bearer token; `json:"-"`, never sent to the frontend),
expiry, display username, and a `SessionID` (the graph-cache key — see [[kiali-graph-engine]]).
`UserSessions` is `map[string]*UserSessionData` keyed by **cluster name** (multi-cluster per-user
sessions; partially implemented — see the multi-session KEP). `ErrSubjectMismatch` is an
`errors.Is`-testable sentinel for token-refresh subject mismatches.
^[raw/articles/kiali-doc-auth-and-security.md]^[raw/articles/kiali-kep-multi-session-auth.md]

## The five strategies (as of 2026-09-17)

| Strategy | Config | Behavior (key points) |
|---|---|---|
| **anonymous** | `anonymous` | No controller file; middleware injects the Kiali SA token per request. Forced in `kiali run` local mode. |
| **token** | `token` | POST `token` form field, validated by listing namespaces; re-validated per request; `sub` (minus `system:serviceaccount:`) is the display name; lifetime from `conf.LoginToken.ExpirationSeconds`. |
| **header** | `header` | Pre-authenticating proxies: `Authorization` + `Impersonate-*` forwarded to K8s; authenticity via TokenReview (`GetTokenReview`), no Kiali RBAC; `ValidateSession` is **stateless** (valid while the `Authorization` header is present, even with an expired cookie); `Kiali-User` audit always uses the freshly re-verified subject. |
| **openshift** | `openshift` | Authorization-code flow against OpenShift OAuth; `/api/auth/redirect[/{cluster}]` -> PKCE in a SameSite=Lax nonce cookie -> IdP; callback stores the `oauth2.Token` in the encrypted cookie. `ValidateSession` priority: `Authorization` (third-party) -> `oauth_token` query param (mask it) -> own cookie. **Home cluster session required**; remote-only rejected (mesh-only creds: open TODO). |
| **openid** | `openid` | Authorization-code flow only (Keycloak, Dex, Google, ...). See below. |

^[raw/articles/kiali-doc-auth-and-security.md]

## OIDC flow detail

- **State/redirect**: `cachedOpenIdMetadata`/`cachedOpenIdKeySet` are `atomic.Pointer[T]` +
`singleflight` (no mutex, no thundering herd); an empty `web_fqdn` fires a startup warning
(redirect URI derived from spoofable `Host` headers). Redirect fetches
`<issuer>/.well-known/openid-configuration` (cached, singleflight), uses a 15-char nonce and
**mandatory PKCE** (RFC 7636, 43-char verifier, SHA-256 challenge — a missing verifier cookie
hard-fails), sets two SameSite=Lax cookies (`kiali-token-nonce-<cluster>`,
`kiali-token-pkce-verifier-<cluster>`) and CSRF state = `SHA-224(nonce + timestamp + signingKey) +
timestamp`; discovery override (#8777) is explicit
`discovery_override.{authorization,token}_endpoint` > deprecated `authorization_endpoint`
(redirect only) > standard discovery. - **Callback** (`openidFlowHelper` chain): param extraction
-> presence checks -> cookie cleanup -> state/CSRF recheck -> token request -> id_token claim
parse -> **nonce replay check** -> optional `hd`/email allowlist -> privilege check -> session
creation (encrypted cookie). - **RBAC**: *enabled* (default) — the OIDC token (id or access, per
`auth.openid.api_token`) **is** the Kubernetes token; login rejected if the user sees zero
namespaces. *disabled* — the id_token is validated in-house (RS256 + `kid` required; JWKS in
`atomic.Pointer`, refreshed on unknown `kid`) and the Kiali SA token is used for everything, so
all authenticated users share one permission set; `ValidateSession` wraps missing tokens as
`ErrSessionNotFound`, subject/non-string-`username_claim` mismatches as `ErrSubjectMismatch`, and
skips the whole JWT sanity block for `api_token: access_token` (opaque token — integrity relies on
the IdP). **Client secret rotation**: `auth.openid.client_secret` is a `config.Credential` —
mounted from a Secret at `/kiali-secret/oidc-secret` it is re-read on every token exchange (see
CredentialManager below).

^[raw/articles/kiali-doc-auth-and-security.md]

## Session persistence: cookies only

All strategies share `cookieSessionPersistor[T]` (`session_persistor.go`) — **no server-side
session store**; the whole session lives in browser cookies. **Encryption** is AES-GCM keyed by
`conf.LoginToken.SigningKey` (must be 16/24/32 bytes — AES-128/192/256); the cipher is rebuilt per
read/write so **signing-key rotation needs no pod restart**. **Write** serializes `SessionData` ->
AES-GCM -> base64 -> **3584-byte chunks** (browsers cap cookies ~4 KB) into `kiali-token`,
`kiali-token-<cluster>-1..N`, plus a `kiali-token-chunks-<cluster>` counter; all cookies are
`HttpOnly`, `SameSite=Strict`, `Path=<webRoot>`, `Secure` under HTTPS. The cookie inventory is
those session chunks + counter, plus `kiali-token-nonce-<cluster>` (CSRF/replay) and
`kiali-token-pkce-verifier-<cluster>`. **Read** reassembles -> decrypts -> validates the
**strategy name still matches config** (stale sessions after a strategy change are terminated,
`MaxAge=-1`) and that the session is **not expired**; `ReadAllSessions` (multi-cluster) walks all
`kiali-token*` cookies, attempts decrypt on each, silently skips failures (chunk suffixes are
indistinguishable from cluster names by name alone), same gates per session. **Terminate**
overwrites every `kiali-token*` cookie with `MaxAge=-1` and leaves the nonce/PKCE cookies to the
controllers.
^[raw/articles/kiali-doc-auth-and-security.md]

## Context propagation & audit

`handlers/authentication/context.go` defines `ContextKeyAuthInfo` (`map[string]*api.AuthInfo` per
cluster — consumed by `getLayer` in `handlers/utils.go` to build the per-user `business.Layer`)
and `ContextKeySessionID` (the UUID, consumed by the graph cache). All non-anonymous
`ValidateSession`s set the internal `Kiali-User` header for audit (header strategy: fresh
re-verification, warn+continue on failure; openid/token: stored subject; `r.Header.Set` avoids
header duplication).
^[raw/articles/kiali-doc-auth-and-security.md]

## JWT package

`jwt/` wraps `go-jose/v4/jwt` enforcing an **algorithm allowlist** (`ES256/384/512, EdDSA,
HS256/384/512, PS256/384/512, RS256/384/512`) on parse; `ParseSigned` (claims with/without
verification) and `ParseSignedCompact` (raw JWS for the in-house JWKS verification path).
Verification is left to the caller: the Kubernetes API (RBAC-on) or `jws.Verify` (RBAC-off).
^[raw/articles/kiali-doc-auth-and-security.md]

## TLS policy resolution (`tlspolicy/`)

`tlspolicy.Resolve` computes Kiali's **own HTTPS listener** config (not mesh mTLS — that is
`business/tls.go` reading `PeerAuthentication`/`DestinationRule`): `source: config` (explicit
`min_version`/`max_version`, 1.0/1.1 rejected; ciphers in IANA or OpenSSL notation, unknown names
logged+skipped; TLS 1.3 min -> cipher config skipped, Go manages it) or `source: auto`
(**OpenShift only**: reads the `APIServer` `TLSSecurityProfile` `Old`/`Intermediate`
(default)/`Modern`/`Custom`, translating OpenSSL names via a built-in `opensslToIANA` map).
`TLSPolicy.ApplyTo` mutates `tls.Config`; cipher resolution/defaults are lazily built under
`sync.Once`.
^[raw/articles/kiali-doc-auth-and-security.md]

## External service credentials & Istio cert info

`config/security/` types for calling Prometheus/Grafana/tracing: `Credentials` (user/pass XOR
bearer token; `GetHTTPAuthHeader()`), `Identity` (client cert/key for mTLS out), `TLS`
(`skip_certificate_validation`); the `Token` field is a plain string — rotation happens one level
up via `conf.GetCredential` in `util/httputil`. The Mesh page control-plane panel surfaces the
Istio CA root cert: `istio/discovery.go` fetches the `istio-ca-root-cert` ConfigMap's
`root-cert.pem`, `models.Certificate.Parse()` extracts issuer/validity/DNS names, and the frontend
`IstioCertsInfo` renders it; an RBAC-blocked ConfigMap yields a warning + empty certificate list,
not a fatal error.
^[raw/articles/kiali-doc-auth-and-security.md]

## CredentialManager — secret rotation without restarts

`config.Credential` (string typedef, `config/credentials.go`): **values starting with `/` are file
paths** (read + cached); anything else is an inline literal. Callers must use
`conf.GetCredential(field)` — used for `Auth.Token`, `Auth.Password`, `Auth.CertFile/KeyFile`,
`LoginToken.SigningKey`, `Auth.OpenId.ClientSecret`, ... CA bundle paths depend on strategy
(openshift: `additional-ca-bundle.pem` + `oauth-server-ca.crt` + `service-ca.crt` + the pod's
service CA; openid: `additional-ca-bundle.pem` + `openid-server-ca.crt`; else:
`additional-ca-bundle.pem`) — all under the projected `/kiali-cabundle/` volume; missing files are
expected and skipped, and a failed initial pool build does **not** abort startup (system CAs,
watcher stays live for auto-recovery). **Why watch `..data`**: K8s secret mounts are `file ->
..data/file` symlinks; rotation swaps the `..data` symlink atomically, so per-file symlinks never
change and `fsnotify` on them never fires — on a `..data` event `refreshDir` re-reads every cached
file in that dir (symlinks now resolve to new content); non-K8s direct writes keep the old value
and retry next event. **Cert pool**: `rebuildCertPool()` merges system CAs + bundles best-effort
(invalid/missing logged, not fatal) into an `*x509.CertPool` **swapped atomically** —
`GetCertPool()` returns the shared pointer, callers treat it as read-only (cloning per request is
too expensive; the old pointer stays valid for in-flight handshakes until GC);
`validateCertificate` enforces a CA, not expired (pre-staged not-yet-valid warned), RSA >= 2048 /
ECDSA >= 256 / Ed25519, DSA rejected, `CertSign` if `KeyUsage` present. **SA token rotation**:
with `auth.use_kiali_token`, the projected `BearerTokenFile` path is the token value;
`conf.GetCredential` reads + watches it for kubelet rotation. **Audit**: `auditRotation` emits
structured events (group `credential-rotation`, `operation: ROTATE|ROTATE_FAILED`, `type`, `path`)
**only when `server.audit_log` is on**; `conf.Close()` closes the done channel + fsnotify watcher,
`closeOnce` for idempotency.

^[raw/articles/kiali-doc-auth-and-security.md]

## Caching

Kiali keeps a set of layered caches — mesh metadata, per-cluster controller-runtime informer
caches, Prometheus/Tempo request-rate and trace caches, and a per-session in-memory graph cache
with background refresh. The full model (what is cached, what is never cached, RBAC and secrets
rules) is documented in [[kiali-caching]]; the graph-cache mechanics and per-session keying
rationale live in [[kiali-graph-engine]].

## Related

- [[kiali-caching]] — the full caching model (ex-Part 2 of this page) - [[kiali-architecture]] —
backend startup, middleware, client factory - [[kiali-operator]] — deployment and operator-managed
installs - [[kiali-graph-engine]] — the per-session graph cache and its request flow

## Open questions / watch items

- Multi-session auth KEP: 2 of 6 roadmap items done as of the 2026-09-17 ingest; mesh-cluster-only
login (no mgmt-cluster creds) is an open TODO in the OpenShift controller. 2.31.0 shipped an
OpenID/Keycloak logout fix and 2.30.0 shipped OpenShift impersonation for multi-cluster auth —
auth behavior is actively moving; re-verify against the release notes before writing operator
runbooks.
  ^[raw/articles/kiali-docs-news-release-notes.md]
