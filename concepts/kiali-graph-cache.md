---
title: Kiali Graph Cache & Background Refresh
created: 2026-09-17
updated: 2026-09-17
type: concept
tags: [kiali, graph, caching]
sources:
  - raw/articles/kiali-doc-graph-engine.md
  - raw/articles/kiali-kep-graph-cache.md
  - raw/articles/kiali-docs-features-topology.md
  - raw/articles/kiali-doc-STATUS.md
confidence: high
---

# Kiali Graph Cache & Background Refresh

Design history: the **Graph Cache KEP** (`design/KEPS/graph-cache/`, shipped)
motivated this — graph generation can take 30+ s at scale (many Prometheus
queries, appender processing, multi-cluster aggregation), and users re-request
near-identical graphs. Non-goals were caching every combination, "favorite"
pre-computed graphs, bypassing RBAC, or changing the generation algorithm;
it builds on (the still-open) Controller Model KEP.
^[raw/articles/kiali-kep-graph-cache.md]

**What is cached: only namespace graphs.** Node-detail graphs (`GraphNode`)
are always generated fresh. Caching is **per browser session** — keyed by the
session cookie value (`SessionID`) — a deliberate security choice: users have
different RBAC scopes, so sharing a cache across users could leak one user's
namespace view into another's. Multiple tabs in one browser share one cached
graph; different browsers/incognito get separate sessions. Enabled by default
under the deliberately obscure internal path `kiali_internal.graph_cache`
(defaults: `refresh_interval: "60s"`, `inactivity_timeout: "10m"`,
`max_cache_memory_mb: 1000`; `enabled: true`).
^[raw/articles/kiali-doc-graph-engine.md]

### Implementation (`graph/graph_cache.go`, `graph/refresh_job.go`)

- `GraphCacheImpl` holds `sessionGraphs map[string]*CachedGraph` under an
  `RWMutex`; created by `NewGraphCache` in `routing/router.go`.
  `GetSessionGraph` updates `LastAccessed`; the internal
  `getSessionGraphInternal` does not (used by the refresh job so background
  ticks don't extend session life).
- Memory: `EstimateGraphMemory` = (nodes × 3 KB + edges × 1 KB) × 1.1,
  computed once per session and reused. Before storing, `checkMemoryLimits`
  LRU-evicts sessions until the projected total is under the cap.
  Counters: `kiali_graph_cache_hits_total`,
  `kiali_graph_cache_misses_total`,
  `kiali_graph_cache_evictions_total`.
- Request flow (`handlers/graph.go:graphNamespacesWithCache`):
  1. cache disabled or no SessionID → generate fresh, no caching;
  2. **historical query** (`queryTime` provided) → bypass cache entirely,
     leaving existing cache/job intact (replay without disrupting live
     refresh);
  3. **client bypass** (`RefreshInterval <= 0`, i.e. user paused auto-refresh)
     → stop the job, evict, generate fresh;
  4. **cache hit + options match** → serve immediately; if the requested
     `RefreshInterval` changed, `job.UpdateInterval(newInterval)`;
  5. **miss / options mismatch** → generate, store, start a new `RefreshJob`.

  `graphOptionsMatch` compares namespaces, duration, graph type,
  inject-service-nodes, idle-edges, boxBy, appenders, rate settings — and
  deliberately ignores `QueryTime` (the background refresh advances the
  window).
- `RefreshJob` (one goroutine per session, managed by a server-wide
  `RefreshJobManager`): first tick fires at **interval/2** (reduces worst-case
  staleness; heuristic, not a guarantee), then a ticker at `interval`. Each
  tick: inactivity check (evict + stop if idle past
  `InactivityTimeout`) → copy options with `QueryTime = now` (the moving
  window) → regenerate via the injected `GraphGenerator` → `SetSessionGraph`
  preserving the original `LastAccessed`. On error: log, keep the stale graph,
  retry next tick. On **panic**: log the stack, evict, stop — the next user
  request becomes a miss and regenerates from scratch (a broken cycle must not
  serve a misleading stale graph). `UpdateInterval` cancels the pending
  ticker, fires after newInterval/2, then swaps the ticker via `resetChan`
  (guarded against concurrent calls). `RefreshJobManager.StopAll()` stops all
  jobs at server shutdown.
- Instrumentation: `GetGraphGenerationTimePrometheusTimer`,
  `GetGraphAppenderTimePrometheusTimer`, `SetGraphNodes`.

^[raw/articles/kiali-doc-graph-engine.md]


## Related

- [[kiali-graph-engine]] — the full pipeline the cache sits in front of
- [[kiali-architecture]] — backend startup, middleware, client factory
- [[kiali-features]] — user-facing feature map
- [[kiali-keps]] — the Graph Cache KEP (shipped) and the Controller Model KEP
