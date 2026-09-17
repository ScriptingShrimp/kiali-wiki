---
source_url: https://kiali.io/news/release-notes/
ingested: 2026-09-17
sha256: f3ff8bd871a4c08a7ee60251c669e0e4845234a87a206985559b91a218f639fd
note: saved as raw HTML (page is JS-rendered); clean markdown version at kiali-docs-news-release-notes.md
---
<!doctype html>
<html itemscope itemtype="http://schema.org/WebPage" lang="en" class="no-js">
  <head>
    <meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="robots" content="index, follow">


<link rel="shortcut icon" href="/favicons/favicon.ico" >
<link rel="apple-touch-icon" href="/favicons/apple-touch-icon-180x180.png" sizes="180x180">
<link rel="icon" type="image/png" href="/favicons/favicon-16x16.png" sizes="16x16">
<link rel="icon" type="image/png" href="/favicons/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/favicons/android-36x36.png" sizes="36x36">
<link rel="icon" type="image/png" href="/favicons/android-48x48.png" sizes="48x48">
<link rel="icon" type="image/png" href="/favicons/android-72x72.png" sizes="72x72">
<link rel="icon" type="image/png" href="/favicons/android-96x96.png" sizes="96x96">
<link rel="icon" type="image/png" href="/favicons/android-144x144.png" sizes="144x144">
<link rel="icon" type="image/png" href="/favicons/android-192x192.png" sizes="192x192">

<title>Release Notes | Kiali</title>
<meta name="description" content="For additional information check our sprint demo videos and blogs.
2.32.0 Sprint Release: September 14, 2026
Features:
AI: Mesh traffic graph health should use cached health Status Config: Support loading istio configuration from file Scale: Guidance for Pre-Aggregated, federated metrics UI: Mesh page Show Kiali display option UI: Show multiple control planes in Namespaces view during canary upgrade Fixes:
Fix Mesh page duplicate istiod→ztunnel edges when multiple control planes are deployed 2.">
<meta property="og:title" content="Release Notes" />
<meta property="og:description" content="For additional information check our sprint demo videos and blogs.
2.32.0 Sprint Release: September 14, 2026
Features:
AI: Mesh traffic graph health should use cached health Status Config: Support loading istio configuration from file Scale: Guidance for Pre-Aggregated, federated metrics UI: Mesh page Show Kiali display option UI: Show multiple control planes in Namespaces view during canary upgrade Fixes:
Fix Mesh page duplicate istiod→ztunnel edges when multiple control planes are deployed 2." />
<meta property="og:type" content="article" />
<meta property="og:url" content="https://kiali.io/news/release-notes/" /><meta property="article:section" content="news" />

<meta property="article:modified_time" content="2026-09-11T18:31:42-04:00" />

<meta itemprop="name" content="Release Notes">
<meta itemprop="description" content="For additional information check our sprint demo videos and blogs.
2.32.0 Sprint Release: September 14, 2026
Features:
AI: Mesh traffic graph health should use cached health Status Config: Support loading istio configuration from file Scale: Guidance for Pre-Aggregated, federated metrics UI: Mesh page Show Kiali display option UI: Show multiple control planes in Namespaces view during canary upgrade Fixes:
Fix Mesh page duplicate istiod→ztunnel edges when multiple control planes are deployed 2.">
<meta itemprop="dateModified" content="2026-09-11T18:31:42-04:00" />
<meta itemprop="wordCount" content="7277">
<meta itemprop="keywords" content="" /><meta name="twitter:card" content="summary"/><meta name="twitter:title" content="Release Notes"/>
<meta name="twitter:description" content="For additional information check our sprint demo videos and blogs.
2.32.0 Sprint Release: September 14, 2026
Features:
AI: Mesh traffic graph health should use cached health Status Config: Support loading istio configuration from file Scale: Guidance for Pre-Aggregated, federated metrics UI: Mesh page Show Kiali display option UI: Show multiple control planes in Namespaces view during canary upgrade Fixes:
Fix Mesh page duplicate istiod→ztunnel edges when multiple control planes are deployed 2."/>




<link rel="preload" href="/scss/main.min.33b4471d0ae8debd5365169d803bae4686f9811cd773eec2e69dd1ceb22dd0d9.css" as="style">
<link href="/scss/main.min.33b4471d0ae8debd5365169d803bae4686f9811cd773eec2e69dd1ceb22dd0d9.css" rel="stylesheet" integrity="">

<script
  src="https://code.jquery.com/jquery-3.6.3.min.js"
  integrity="sha512-STof4xm1wgkfm7heWqFJVn58Hm3EtS31XFaagaa8VMReCXAkQnJZ+jEy8PCC/iT18dFy95WcExNHFTqLyp72eQ=="
  crossorigin="anonymous"></script>
<script src="
https://cdn.jsdelivr.net/npm/echarts@5.6.0/dist/echarts.min.js
"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-130444728-1"></script>
<script>
var doNotTrack = false;
if (!doNotTrack) {
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());
	gtag('config', 'UA-130444728-1');
}
</script>
  </head>
  <body class="td-page">
    <header>
      <nav class="td-navbar navbar-dark js-navbar-scroll">
<div class="container-fluid flex-column flex-md-row">
  <a class="navbar-brand" href="/"><span class="navbar-brand__logo navbar-logo"><svg id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 1280" style="enable-background:new 0 0 1280 1280"><style>.st0{fill:#013144}.st1{fill:#0093dd}</style><g><path class="st0" d="M810.9 180.9c-253.6.0-459.1 205.5-459.1 459.1s205.5 459.1 459.1 459.1S1270 893.6 1270 640 1064.5 180.9 810.9 180.9zm0 848.3c-215 0-389.2-174.3-389.2-389.2.0-215 174.3-389.2 389.2-389.2S1200.1 425 1200.1 640s-174.2 389.2-389.2 389.2z"/><path class="st1" d="M653.3 284c-136.4 60.5-231.6 197.1-231.6 356 0 158.8 95.2 295.5 231.6 356 98.4-87.1 160.4-214.3 160.4-356C813.7 498.3 751.6 371.1 653.3 284z"/><path class="st1" d="M351.8 640c0-109.8 38.6-210.5 102.8-289.5-39.6-18.2-83.6-28.3-130-28.3C150.9 322.2 10 464.5 10 640s140.9 317.8 314.6 317.8c46.3.0 90.4-10.1 130-28.3-64.3-79-102.8-179.7-102.8-289.5z"/></g></svg></span><span class="navbar-brand__name">Kiali</span></a>
  <div class="td-navbar-nav-scroll ms-md-auto" id="main_navbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="/docs/"><span>Documentation</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link active" href="/news/"><span>News</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/community/"><span>Community</span></a>
      </li>
      <li class="nav-item dropdown d-none d-lg-block">
        <div class="dropdown">
  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Releases</a>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="https://kiali.io">current</a></li>
    <li><a class="dropdown-item" href="https://v2-31.kiali.io">v2.31</a></li>
    <li><a class="dropdown-item" href="https://v2-30.kiali.io">v2.30</a></li>
    <li><a class="dropdown-item" href="https://v2-29.kiali.io">v2.29</a></li>
    <li><a class="dropdown-item" href="https://v2-28.kiali.io">v2.28</a></li>
    <li><a class="dropdown-item" href="https://v2-27.kiali.io">v2.27  [ossm 3.4]</a></li>
    <li><a class="dropdown-item" href="https://v2-26.kiali.io">v2.26  [istio v1.30]</a></li>
    <li><a class="dropdown-item" href="https://v2-22.kiali.io">v2.22 [ossm 3.3]</a></li>
    <li><a class="dropdown-item" href="https://v2-21.kiali.io">v2.21 [istio v1.29]</a></li>
    <li><a class="dropdown-item" href="https://v2-17.kiali.io">v2.17 [istio v1.28, ossm 3.2]</a></li>
    <li><a class="dropdown-item" href="https://v2-12.kiali.io">v2.12 [istio v1.27]</a></li>
    <li><a class="dropdown-item" href="https://v2-11.kiali.io">v2.11  [ossm v3.1]</a></li>
    <li><a class="dropdown-item" href="https://v2-4.kiali.io">v2.4 [ossm v3.0]</a></li>
    <li><a class="dropdown-item" href="https://staging.kiali.io">staging</a></li>
    <li><a class="dropdown-item" href="https://pre-v1-41.kiali.io">archive</a></li>
    </ul>
</div></li>
      </ul>
  </div>
  <div class="d-none d-lg-block">
    <div class="td-search">
  <div class="td-search__icon"></div>
  <input type="search" class="td-search__input form-control td-search-input" placeholder="Search this site…" aria-label="Search this site…" autocomplete="off">
</div>
  </div>
</div>
</nav>
    </header>
    <div class="container-fluid td-outer">
      <div class="td-main">
        <div class="row flex-xl-nowrap">
          <aside class="col-12 col-md-3 col-xl-2 td-sidebar d-print-none">
            <div id="td-sidebar-menu" class="td-sidebar__inner">
  <form class="td-sidebar__search d-flex align-items-center">
    <div class="td-search">
  <div class="td-search__icon"></div>
  <input type="search" class="td-search__input form-control td-search-input" placeholder="Search this site…" aria-label="Search this site…" autocomplete="off">
</div>
    <button class="btn btn-link td-sidebar__toggle d-md-none p-0 ms-3 fas fa-bars" type="button" data-bs-toggle="collapse" data-bs-target="#td-section-nav" aria-controls="td-section-nav" aria-expanded="false" aria-label="Toggle section navigation">
    </button>
  </form>
  <nav class="td-sidebar-nav collapse foldable-nav" id="td-section-nav">
    <ul class="td-sidebar-nav__section pe-md-3 ul-0">
      <li class="td-sidebar-nav__section-title td-sidebar-nav__section with-child active-path" id="m-news-li">
  <a href="/news/" class="align-left ps-0 td-sidebar-link td-sidebar-link__section tree-root" id="m-news"><span class="">News</span></a>
  <ul class="ul-1">
    <li class="td-sidebar-nav__section-title td-sidebar-nav__section without-child active-path" id="m-newsrelease-notes-li">
  <input type="checkbox" id="m-newsrelease-notes-check" checked/>
  <label for="m-newsrelease-notes-check"><a href="/news/release-notes/" class="align-left ps-0  active td-sidebar-link td-sidebar-link__page" id="m-newsrelease-notes"><span class="td-sidebar-nav-active-item">Release Notes</span></a></label>
  
</li><li class="td-sidebar-nav__section-title td-sidebar-nav__section with-child" id="m-newssecurity-bulletins-li">
  <input type="checkbox" id="m-newssecurity-bulletins-check"/>
  <label for="m-newssecurity-bulletins-check"><a href="/news/security-bulletins/" class="align-left ps-0  td-sidebar-link td-sidebar-link__section" id="m-newssecurity-bulletins"><span class="">Security Bulletins</span></a></label>
  
  <ul class="ul-2 foldable">
    <li class="td-sidebar-nav__section-title td-sidebar-nav__section without-child" id="m-newssecurity-bulletinskiali-security-003-li">
  <input type="checkbox" id="m-newssecurity-bulletinskiali-security-003-check"/>
  <label for="m-newssecurity-bulletinskiali-security-003-check"><a href="/news/security-bulletins/kiali-security-003/" class="align-left ps-0  td-sidebar-link td-sidebar-link__page" id="m-newssecurity-bulletinskiali-security-003"><span class="">KIALI-SECURITY-003 - Installation into ad-hoc namespaces</span></a></label>
  
</li><li class="td-sidebar-nav__section-title td-sidebar-nav__section without-child" id="m-newssecurity-bulletinskiali-security-002-li">
  <input type="checkbox" id="m-newssecurity-bulletinskiali-security-002-check"/>
  <label for="m-newssecurity-bulletinskiali-security-002-check"><a href="/news/security-bulletins/kiali-security-002/" class="align-left ps-0  td-sidebar-link td-sidebar-link__page" id="m-newssecurity-bulletinskiali-security-002"><span class="">KIALI-SECURITY-002 - Authentication bypass when using the OpenID login strategy</span></a></label>
  
</li><li class="td-sidebar-nav__section-title td-sidebar-nav__section without-child" id="m-newssecurity-bulletinskiali-security-001-li">
  <input type="checkbox" id="m-newssecurity-bulletinskiali-security-001-check"/>
  <label for="m-newssecurity-bulletinskiali-security-001-check"><a href="/news/security-bulletins/kiali-security-001/" class="align-left ps-0  td-sidebar-link td-sidebar-link__page" id="m-newssecurity-bulletinskiali-security-001"><span class="">KIALI-SECURITY-001 - Authentication bypass using forged credentials</span></a></label>
  
</li>
  </ul>
</li>
  </ul>
</li>
    </ul>
  </nav>
</div>

          </aside>
          <aside class="d-none d-xl-block col-xl-2 td-sidebar-toc d-print-none">
            
<div class="td-page-meta ms-2 pb-1 pt-2 mb-0">
<a href="https://github.com/kiali/kiali.io/tree/staging/content/en/news/release-notes.md" class="td-page-meta--view" target="_blank" rel="noopener"><i class="fa-solid fa-file-lines fa-fw"></i> View page source</a>
  <a href="https://github.com/kiali/kiali.io/edit/staging/content/en/news/release-notes.md" class="td-page-meta--edit" target="_blank" rel="noopener"><i class="fa-solid fa-pen-to-square fa-fw"></i> Edit this page</a>
  <a href="https://github.com/kiali/kiali.io/new/staging/content/en/news?filename=change-me.md&amp;value=---%0Atitle%3A&#43;%22Long&#43;Page&#43;Title%22%0AlinkTitle%3A&#43;%22Short&#43;Nav&#43;Title%22%0Aweight%3A&#43;100%0Adescription%3A&#43;%3E-%0A&#43;&#43;&#43;&#43;&#43;Page&#43;description&#43;for&#43;heading&#43;and&#43;indexes.%0A---%0A%0A%23%23&#43;Heading%0A%0AEdit&#43;this&#43;template&#43;to&#43;create&#43;your&#43;new&#43;page.%0A%0A%2A&#43;Give&#43;it&#43;a&#43;good&#43;name%2C&#43;ending&#43;in&#43;%60.md%60&#43;-&#43;e.g.&#43;%60getting-started.md%60%0A%2A&#43;Edit&#43;the&#43;%22front&#43;matter%22&#43;section&#43;at&#43;the&#43;top&#43;of&#43;the&#43;page&#43;%28weight&#43;controls&#43;how&#43;its&#43;ordered&#43;amongst&#43;other&#43;pages&#43;in&#43;the&#43;same&#43;directory%3B&#43;lowest&#43;number&#43;first%29.%0A%2A&#43;Add&#43;a&#43;good&#43;commit&#43;message&#43;at&#43;the&#43;bottom&#43;of&#43;the&#43;page&#43;%28%3C80&#43;characters%3B&#43;use&#43;the&#43;extended&#43;description&#43;field&#43;for&#43;more&#43;detail%29.%0A%2A&#43;Create&#43;a&#43;new&#43;branch&#43;so&#43;you&#43;can&#43;preview&#43;your&#43;new&#43;file&#43;and&#43;request&#43;a&#43;review&#43;via&#43;Pull&#43;Request.%0A" class="td-page-meta--child" target="_blank" rel="noopener"><i class="fa-solid fa-pen-to-square fa-fw"></i> Create child page</a>
  <a href="https://github.com/kiali/kiali.io/issues/new?title=Release%20Notes" class="td-page-meta--issue" target="_blank" rel="noopener"><i class="fa-solid fa-list-check fa-fw"></i> Create documentation issue</a>
  <a href="https://github.com/kiali/kiali/issues/new" class="td-page-meta--project-issue" target="_blank" rel="noopener"><i class="fa-solid fa-list-check fa-fw"></i> Create project issue</a>
  <a id="print" href="/news/_print/"><i class="fa-solid fa-print fa-fw"></i> Print entire section</a>

</div>

            <div class="td-toc">
        <nav id="TableOfContents">
  <ul>
    <li><a href="#2320">2.32.0</a></li>
    <li><a href="#2310">2.31.0</a></li>
    <li><a href="#2300">2.30.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2290">2.29.0</a></li>
    <li><a href="#2280">2.28.0</a></li>
    <li><a href="#2270">2.27.0</a></li>
    <li><a href="#2260">2.26.0</a></li>
    <li><a href="#2250">2.25.0</a></li>
    <li><a href="#2240">2.24.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2230">2.23.0</a></li>
    <li><a href="#2220">2.22.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2210">2.21.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2200">2.20.0</a></li>
    <li><a href="#2190">2.19.0</a></li>
    <li><a href="#2180">2.18.0</a></li>
    <li><a href="#2170">2.17.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2160">2.16.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2150">2.15.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2140">2.14.0</a>
      <ul>
        <li></li>
      </ul>
    </li>
    <li><a href="#2130">2.13.0</a></li>
    <li><a href="#2120">2.12.0</a></li>
    <li><a href="#2110">2.11.0</a></li>
    <li><a href="#2100">2.10.0</a></li>
    <li><a href="#290">2.9.0</a></li>
    <li><a href="#280">2.8.0</a></li>
    <li><a href="#270">2.7.0</a></li>
    <li><a href="#260">2.6.0</a></li>
    <li><a href="#250">2.5.0</a></li>
    <li><a href="#240">2.4.0</a></li>
    <li><a href="#230">2.3.0</a></li>
    <li><a href="#220">2.2.0</a></li>
    <li><a href="#210">2.1.0</a></li>
    <li><a href="#200">2.0.0</a></li>
    <li><a href="#1894">1.89.4</a></li>
    <li><a href="#1893">1.89.3</a></li>
    <li><a href="#1890">1.89.0</a></li>
    <li><a href="#1880">1.88.0</a></li>
    <li><a href="#1870">1.87.0</a></li>
    <li><a href="#1860">1.86.0</a></li>
    <li><a href="#1850">1.85.0</a></li>
    <li><a href="#1840">1.84.0</a></li>
    <li><a href="#1830">1.83.0</a></li>
    <li><a href="#1820">1.82.0</a></li>
    <li><a href="#1810">1.81.0</a></li>
    <li><a href="#1800">1.80.0</a></li>
    <li><a href="#1790">1.79.0</a></li>
    <li><a href="#1780">1.78.0</a></li>
    <li><a href="#1770">1.77.0</a></li>
    <li><a href="#1760">1.76.0</a></li>
    <li><a href="#1750">1.75.0</a></li>
    <li><a href="#1740">1.74.0</a></li>
  </ul>
</nav>
      </div>
    
            
	
          </aside>
          <main class="col-12 col-md-9 col-xl-8 ps-md-5" role="main">
            
  

            <nav aria-label="breadcrumb" class="td-breadcrumbs">
  <ol class="breadcrumb">
  <li class="breadcrumb-item">
    <a href="/news/">News</a></li>
  <li class="breadcrumb-item active" aria-current="page">
    Release Notes</li>
  </ol>
</nav>
            
<div class="td-content">
	<h1>Release Notes</h1>
	
	<header class="article-meta">
		
  </header>
	<p>For additional information check our <a href="https://www.youtube.com/channel/UCcm2NzDN_UCZKk2yYmOpc5w">sprint demo videos</a> and <a href="https://medium.com/kialiproject">blogs</a>.</p>
<h2 id="2320">2.32.0</h2>
<p>Sprint Release: September 14, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/10097">AI: Mesh traffic graph health should use cached health Status</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8440">Config: Support loading istio configuration from file</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6342">Scale: Guidance for Pre-Aggregated, federated metrics</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9662">UI: Mesh page Show Kiali display option</a></li>
<li><a href="https://github.com/kiali/kiali/pull/10270">UI: Show multiple control planes in Namespaces view during canary upgrade</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/10286">Fix Mesh page duplicate istiod→ztunnel edges when multiple control planes are deployed</a></li>
</ul>
<h2 id="2310">2.31.0</h2>
<p>Release: August 21, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/10139">AI: Automate MCP pin compatibility validation (replace manual contract tests)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9193">API: Perform robust and consistent query param validation</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/808">OSSMC: Add fleet mesh and multi-mesh capabilities</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/790">OSSMC: Monaco editor loads worker scripts from external CDN instead of local bundle</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6817">UI: Show the message only once in Messaging center</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9711">UI: Support glass and high contrast themes for OSSMC/OpenShift 5.0</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6091">UI: Hide inbound traffic data when inspecting ingress gateway nodes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10124">Validations: ignore Sidecar egress import scope (false positives under locked-down Sidecar)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10132">Operator: Make the operator pod&rsquo;s probe timings configurable in the helm chart</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/10144">Ambient: KIA1313 false positive never clears: validation change detection does not track waypoint resolution, leaving stale results in the validations store</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10095">Auth: OpenID strategy with Keycloak never logout from Kiali UI</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/803">OSSMC: Local dev fails to load OverviewPage after Kiali 2.31 sync (GraphShortcuts setExtraStackFrame)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10151">UI: Several small UI/navigation bugs in the Kiali frontend</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10155">UI: Fix Grafana Explore deep-link</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10183">Validations: KIA0102 false positive with wildcard methods</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10188">Validations: Istio validation false positives (P0): AuthZ hosts, auto-mTLS, appProtocol, Gateway API</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10189">Validations: Istio validation false positives (P1): AuthZ namespaces, RequestAuth merge, selectors, subsets</a></li>
</ul>
<h2 id="2300">2.30.0</h2>
<p>Release: August 03, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9135">AI: Enhance AI Chatbot: Context Awareness &amp; UX Improvements</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9149">AI: Implement Streaming Responses for Chatbot to Display Real-Time MCP Tool Execution Status</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9371">AI: Reduce Output Payload Size</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9976">AI: Multi-cluster eval test suite for Kiali MCP</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7900">Ambient: Disable L7 istio configs for services that are in Ambient but doesn&rsquo;t have a waypoint proxy</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9859">K8s GW API v1.6.0 support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10038">OpenShift: OpenShift Impersonation for Multi-Cluster Auth</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10016">UX: Remove refresh interval from Istio Config editor page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5309">Validation: Annotations for ignoring Kiali Errors/Warnings in the console?</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/10072">Health: Custom config: failure: 0 does not trigger Failure status despite docs saying it should</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10041">UI: Annotation editor: follow-up fixes from #10010 review</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10008">UI: Pods not shown for Argo Rollouts configured via custom_workload_types</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10098">Validation: Istio configs per namespace returns validations for all the cluster</a></li>
</ul>
<h4 id="upgrade-change-notes">Upgrade Change Notes:</h4>
<p>The fix for custom health status configuration could affect existing users. Degraded health status could now be reported
as Failure. The behavior is correct, but could be unexepected. If affected, ensure proper setting of the failure threshold
in your custom health configuration.</p>
<h2 id="2290">2.29.0</h2>
<p>Release: July 13, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9622">Ambient: v1.30 support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9895">AI: Enhance support for multi cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9910">AI: Implement Ask/Troubleshooting Mode Selection with Provider-Specific Prompts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9945">AI: Token reduction</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9946">AI: Add Gateway API support to MCP tools</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9941">AI: Improve error handling in multiple tool calls</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9974">AI: Make the AI MCP max tool iterations configurable</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9977">AI: Enhance MCP Server with Istio Ambient Mesh Discovery and Debugging Capabilities</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9722">API: Remove includeAmbient from metrics options and use reporter</a></li>
<li><a href="https://github.com/kiali/kiali/issues/10009">UX: Improve workload annotation editing by handling controller and tempate annotaions</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9912">UX: Improve Istio Config side panel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9709">UX: Replace react-ace with PatternFly CodeEditor (Monaco)</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9921">AI: &ldquo;Confirm chat deletion&rdquo; modal does not appear when switching from a disconnected AI provider</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9942">AI: MCP regression</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9961">AI: Log debugs with chatgpt</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9929">CI: Error in Test Perses link</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9948">Graph: Find unhealthy workloads — graph find hide</a></li>
<li><a href="https://github.com/kiali/kiali/pull/10015">Graph: Fix issue with faint trace overlay</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9964">Operator: OSSMC plugin installation fails with 401 when server.require_auth: true is set in the Kiali CR</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9953">OSSMC: Crashes in Namespace detail tab</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9937">Validations: KIA1401 false positive for HTTPRoutes whose namespace is enrolled in Ambient mesh</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9986">Validations: KIA1317 should be excluded from waypoint proxies</a></li>
</ul>
<h2 id="2280">2.28.0</h2>
<p>Release: June 22, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9736">AI: Make LightSpeed TLS verification configurable</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9744">AI: Built-in MCP prompts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9753">AI: Use MCP Checker actions instead of the binary</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9623">Ambient: Validate Kiali with Ambient 1.30</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9574">API: GW API IE v1.5.0 Support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9787">Auth: OAuth2 client_credentials: follow-up fixes and improvements across kiali, operator, and helm-charts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9728">I18N: Create i18n conventions file</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9836">Operator: RBAC permission cleanup</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9723">UX: Use filter columns in list pages as in the namespace list page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9800">Validation: Add Kiali Validation for Conflicting ServiceEntries with Same Host and Port but Different Protocols</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9784">Ambient: Ambient Traffic dropdown hidden when home cluster has no ztunnel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9790">Multicluster: Workloads list fails with &ldquo;namespace not accessible&rdquo; when ignore_home_cluster=true</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9819">Validation: KIA1401 false positive when Gateway allowedRoutes selector uses matchExpressions</a></li>
</ul>
<h2 id="2270">2.27.0</h2>
<p>Release: June 01, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9148">AI: Support anthropic provider</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9143">AI: Implement background job to clean stale store data.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9137">AI: Extend resource_details tool to support Application-level resources</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9142">AI: Token Usage Analytics</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9141">AI: Harden System Prompt Against Injection</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6895">Kiali.io: Update Istio Configuration Section</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9040">Mesh page: Multi-mesh Control Plane Donut chart support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9701">Perf: Improve in point traffic animation</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8524">Perf: Improve &ldquo;istio&rdquo; graph appender performance</a></li>
<li><a href="https://github.com/kiali/kiali/pull/9765">Perf: Improve health cache memory utilizion</a></li>
<li><a href="https://github.com/kiali/kiali/pull/9766">Perf: Improve workload fetching for single namespaces</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9716">Server: Re-enable Prometheus after initial health check failure</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9655">UX: Improve wizard buttons in view-only mode</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9646">UX: Update detail pages in the style of the new Namespace detail page</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9624">UI: Clicking chart data points throws TypeError</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9685">UI: No heatmap in some Ambient tracing namespace</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9691">UI: Show &ldquo;No related resources&rdquo; message in the Related card when empty</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9714">UI: (Mesh page) ztunnel not connected with the control plane</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9674">Validation: (Ambient) False positive in KIA1313</a></li>
</ul>
<p><strong>The following fields are no longer used by the Kiali CR and will be ignored if currently set. The standard constant values are now used.</strong></p>
<ul>
<li><code>spec.istio_labels.egress_gateway_label</code></li>
<li><code>spec.istio_labels.ingress_gateway_label</code></li>
<li><code>spec.istio_labels.injection_label_name</code></li>
<li><code>spec.istio_labels.injection_label_rev</code></li>
</ul>
<h2 id="2260">2.26.0</h2>
<p>Release: May 29, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9148">AI: Support anthropic provider</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9144">AI: Support Google Model Provider</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9143">AI: Implement background job to clean stale store data</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9504">Ambient: Trace overlay</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7514">Config: identity domain</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9590">Config: Add pod disruption budget template to kiali chart</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8654">Deployment: Add ability to enable/disable prometheus</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9162">Overview Page: Follow-up UX improvements</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/631">OSSMC: Add Namespace and Application list pages to OSSMC</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/654">OSSMC: Replace native Istio Config list page with Kiali&rsquo;s IstioConfigListPage</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6915">Perf: trace hover tooltip performance boost</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9575">UI: Replace height magic numbers with CSS flex layout</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9588">UI: Traffic menu design iteration</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9610">UI: Add Namespace Detail page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5688">UI: Better support for annotation and label editing</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9150">AI: Fix Hallucinated/Broken Text Links in Chatbot Navigation Responses</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9582">AI: Return in MCPtools error type when token is not valid</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9658">Ambient: ztunnel dump error</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/638">OSSMC: Cluster name not shown on Istio Config Details page in OSSMC</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9647">OSSMC: MTLS icon is not working</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9586">UI: Chart legend toggle stops responding after two clicks</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9581">UI: Unreadable Text for Istio Validations</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9631">UI: tracing: Incorrect visualization of tooltip</a></li>
</ul>
<h2 id="2250">2.25.0</h2>
<p>Release: April 20, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9507">Ambient: Improve inter-cluster telemetry</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9145">AI: Implement Unit and Integration tests for Backend API</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5915">Graph: Include inbound and outbound edges when automatically activating rank</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7725">Validation: Multi-primary support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7727">Validations: Multi-primary support for MeshConfig</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9474">UI: Improve Duration handling for fixed-duration pages (lists, overview)</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9521">AI: manage_istio_config returns UI-only actions payload to MCP clients that cannot handle it</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9488">Auth: Kiali uses static bearer token for Prometheus/Tracing auth, breaks with short-lived projected SA tokens</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9476">Server: Kiali Fails to Startup With Health Cache Enabled</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9468">UI: Application link can navigate to workload detail</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9471">UI: workload list health status tooltip always showing 0 pods</a></li>
</ul>
<h2 id="2240">2.24.0</h2>
<p>Release: March 30, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9136">AI: Optimize get_istio_config tool for better parsing and token efficiency</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9250">AI: Handle impact of new Namespaces page.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9328">Build: Upgrade Node.js from v20 to v24</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9111">Build: Migrate from Yarn v1 to Yarn v4</a></li>
<li><a href="https://github.com/kiali/kiali/issues/">Build: Upgrade Golang from v1.24 to v1.25</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9294">Kiali.io: Update docs with changes related to new overview page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8987">Server: Automatically set GOMEMLIMIT based on available memory (container cgroups / system)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9306">UI: Ambient and sidecars badges in the overview/namespaces pages</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9281">UI: Overview Page Service Insights should incorporate L4 metrics</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9360">UI: Overview Page re-order top row cards to group infrastructure</a></li>
<li><a href="https://github.com/kiali/kiali/pull/9355">UI: Improve UX for Graph Display menu</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9099">PF6 misalignment issues</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8500">K8s Client (cluster2) is not found or is not accessible for Kiali, when attempting multi-cluster configuration feature</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9359">(AI)(Tool) get_resource_detail: Remove &lsquo;istio&rsquo; and &lsquo;app&rsquo; from allowed resourceTypes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9363">(AI)(Tool)(Panic) get_mesh_graph throw panic when the namespace not exist</a></li>
</ul>
<h4 id="upgrade-change-notes-1">Upgrade Change Notes:</h4>
<p><strong>kiali_health_status metric</strong></p>
<p>Starting in v2.22, when the health cache and kiali metrics are both enabled (true by default) Kiali would also write a new metric, <code>kiali_health_status</code>. The initial implementation proved to be too heavy from a cardinality perspective. This metric has been redefined in v2.24 and will now generate a much lower cardinality of time series. Also, it is now opt-in, controlled by <code>spec.server.observability.metrics.health_status.enabled</code>. So, by default in v2.24, this metric will be disabled. The metric name remains the same, although attributes have been altered. Unless manually manipulated, existing series will remain in Prometheus until they naturally expire.</p>
<h2 id="2230">2.23.0</h2>
<p>Release: March 09, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9138">AI: Implement get_resource_metrics tool for CPU and Memory monitoring.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9140">AI: Implement get_logs tool for retrieving pod/container logs.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9147">AI: Comprehensive documentation for features.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9153">AI: Integrate Chatbot AI into new Overview and Namespace pages</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9275">API: K8s GW API to v1.5.0</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9189">OSSMC: New Overview page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9261">Security: Update to Go v1.24.13</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6922">Server: Remove Istio Service Registry dependency on Validations</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8845">UI: New Overview and Namespaces Pages</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9297">Multiple Kiali metric-calculation defects produce incorrect user-visible values</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9236">remove root_namespace section in docs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9276">Nil pointer dereference in SubsetPresenceChecker when VirtualService has nil route destinations</a></li>
</ul>
<h2 id="2220">2.22.0</h2>
<p>Release: February 16, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9079">AI: Implement AI Chatbot Widget &amp; MCP Integration (Dev Preview)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8900">Perf: Introduce health pre-compute</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9158">Tracing: new use_waypoint_name config option (incorrect service name in Jaeger link)</a></li>
<li><a href="https://github.com/kiali/kiali/pull/9067">UI: SPIRE support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9098">UI: Replace react-datepicker with PatternFly 6 components</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9070">UI: Slow loading of workloads</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9091">UI: PF6 Wizard Migration Issues</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9171">UI: Offline mode does not display Istio Config page</a></li>
</ul>
<h4 id="upgrade-change-notes-2">Upgrade Change Notes:</h4>
<p><strong>Health Status Pre-Compute and Caching</strong></p>
<p>Kiali v2.22 introduces health status pre-compute and caching which is enabled by default. Production mesh sizes are growing and Kiali render times have been increasing, particularly for the Overview and List pages. In response, Kiali v2.22 changes its approach to health status calculation. In prior versions Kiali calculated health &ldquo;on-demand&rdquo;, based on the user&rsquo;s selected duration, configuration settings, and other information, such as pod status. Starting in v2.22 Kiali will pre-calculate health status using a single, configurable duration, 5 minutes by default. The cached values increase the responsiveness of the Overview and List pages. Other pages, such as the Traffic graph and Detail pages will continue to calculate health status on-demand, and is based on the user&rsquo;s selected duration. Users may notice that the Duration Dropdown selector has been removed from the Overview and List pages.</p>
<p>Users may notice an increase in backend resource utilization, as the Kiali server will now be calculating and refreshing health status, independent of user sessions. The Kiali CR introduces the following new configuration:</p>
<p><code>spec.health_config.compute.duration: 5m</code>
<code>spec.health_config.compute.refresh_interval: 3m</code>
<code>spec.health_config.compute.timeout: 10m</code></p>
<p><code>spec.kiali_internal.health_cache.enabled: false</code></p>
<p>It is recommended to keep the health cache enabled, as not all features will fall back to on-demand calculation.</p>
<p>Any questions, comments or feedback appreciated. Visit <code>#kiali</code> on Istio Slack or start a Discussion in Github at <code>https://github.com/kiali/kiali</code>.</p>
<h2 id="2210">2.21.0</h2>
<p>Release: January 26, 2026</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8777">Auth: Provide explicit OIDC config if .well-known/openid-configuration is locked down</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8888">Auth: Use auto-rotated certificates for external service (e.g. prometheus) connectivity</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8421">Auth: Support OpenID Authorization Code Flow with PKCE (SSO)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8871">Perf: Introduce background graph refresh and caching</a></li>
<li><a href="https://github.com/kiali/kiali/pull/9005">Perf: Improve traffic graph client-side rendering, particularly when displaying many service nodes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9033">Security: Enforce platform TLS profiles in Kiali via OpenShift-aware auto mode and kiali config fallback</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8710">UI: Masthead status improved layout and multi-mesh handling</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8979">UI: Notification center improvements for message detail handling</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/9009">Ambient: Fix missing Idle Node display in traffic graph, when not showing Waypoints</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8990">Auth: Session persistor fixes re: chunked sessions and multi-session scenarios</a></li>
<li><a href="https://github.com/kiali/kiali/issues/9014">Perses: Validate OpenShift dashboards</a></li>
</ul>
<h4 id="upgrade-change-notes-3">Upgrade Change Notes:</h4>
<p><strong>Traffic Graph Caching</strong></p>
<p>Kiali v2.21 introduces traffic graph caching. Enabled by default. When a user navigates to the Traffic Graph and renders the initial graph, Kiali will start a background job to regenerate the graph periodically, based on the refresh interval set in the UI. The background job will cache the resulting graph and return it on subsequent UI requests. This can greatly improve re-render times, especially for larger graphs. Note that the initial graph render time will be unchanged. It is still recommended to use &ldquo;Manual&rdquo; refresh when working with large meshes, in order to fully define the desired graph before performing the initial request. Any fundamental change to the graph definition will invalidate the cache and restart a new refresh job. Users can navigate away and then back to the traffic graph, and resume with the latest cached graph, within the timeout period (10m by default).</p>
<p>Backend resource utilization may be affected, although is not anticipated to change significantly. The caching can be disabled in the Kiali config via:</p>
<p><code>spec.kiali_internal.graph_cache.enabled: false</code></p>
<p>Any questions, comments or feedback appreciated. Visit <code>#kiali</code> on Istio Slack or start a Discussion in Github at <code>https://github.com/kiali/kiali</code>.</p>
<h2 id="2200">2.20.0</h2>
<p>Release: December 22, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8539">Maintenance: Upgrade to TypeScript 5</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/518">OSSMC: Upgrade to Patternfly 6</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8022">UI: Upgrade to PatternFly 6</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8911">UI: Replace legacy message center</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8918">GWAPI IE: Errors in Kiali logs when namespace stack</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8903">Mesh Page: sporadic null reference in SummaryPanelClusterBox</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8908">UI: Could not fetch workloads list</a></li>
</ul>
<h2 id="2190">2.19.0</h2>
<p>Release: November 24, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8872">AI: Kiali now has AI and Agent Policy and Contribution guidelines</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8616">Config: Kiali CR now supports adding custom initContainers to the Kiali deployment</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8854">Helm Charts: Server helm chart now supports cluster_wide_access=false</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8791">K8s GW API: v1.4.0 support</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8867">Ambient: Fix &ldquo;isAmbient&rdquo; CP identification and Overview page badging</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8863">Mesh Page: Fix missing validations for Data Plane side-panel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8830">UI: Masthead tooltip fixes for status and duplication</a></li>
</ul>
<h2 id="2180">2.18.0</h2>
<p>Release: November 03, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8684">Mesh Page: improvements for multiple controlplanes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8806">Perses: &lsquo;openshift&rsquo; URL format</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5028">Operator: Sidecar usage extension</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8813">Operator: NetworkPolicy for OLM-installed operator</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/507">OSSMC: Add Netobserv Navigation traffic graph side-panel</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8827">URI too large</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8826">Making cluster-wide namespace query when cluster-wide-access is false</a></li>
</ul>
<h2 id="2170">2.17.0</h2>
<p>Release: October 13, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8717">Auth: Support of multiple audiences in OIDC</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8692">Config: Remove use of conf.ExternalServices.Istio.Registry</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8755">Dependencies: Update GoLang to 1.24.4</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8782">GW API: Support Inference Extension v1</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8668">Mesh Page: Show Kiali when in Local mode</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8762">OSSMC: New &ldquo;openshift&rdquo; url_format for Tracing configuration</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8536">Security: Allow configuration of NetworkPolicy to restrict Kiali ingress traffic</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8468">Troubleshooting: Improve Kiali tracing by forwarding <code>x-request-id</code> header to prometheus calls</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8749">OSSMC: Handle correctly pods page with no controller</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8765">OSSMC: Distributed tracing plugin not doing redirection</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8759">Server: Fix potential crash in Mesh Discovery</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8751">UI: Scroll issue in Istio Config page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8781">UI: Kiali observability detail views not available to custom GVKs</a></li>
</ul>
<h4 id="upgrade-change-notes-4">Upgrade Change Notes:</h4>
<p><strong>The following fields are no longer used by the Kiali CR and MUST be removed, if currently set.</strong></p>
<ul>
<li><code>spec.external_services.istio.registry</code></li>
</ul>
<h2 id="2160">2.16.0</h2>
<p>Release: September 22, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8674">CRD: Autodetect <code>RootNamespace</code></a></li>
<li><a href="https://github.com/kiali/kiali/issues/8655">GatewayAPI: Support clusters that only have Gateway API gateways but no Istio gateways</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8732">Perf: graph &ldquo;Show Virtual Services&rdquo; option controls &ldquo;istio_detail&rdquo; appender execution</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8731">Perf: optimizations for the istio_detail graph appender</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8678">Ambient: Fix validations in KIA1312, KIA1313 and KIA1316</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8700">UI: Fix missing version info in About box</a></li>
</ul>
<h4 id="upgrade-change-notes-5">Upgrade Change Notes:</h4>
<p><strong>Discovery Selectors</strong></p>
<p>Kiali now properly supports Istio control planes deployed into different namespaces. As part of this
support both the <code>spec.istio_namespace</code> and <code>spec.external_services.istio.root_namespace</code> configuration
fields have been removed. As such, Kiali Discovery Selectors, when defined, must include Istio&rsquo;s
control plane namespace(s). If you are using Kiali Discovery Selectors, please ensure that this
new requirement is met. Note that Kiali&rsquo;s deployment namespace is always included, and so co-located
Istio control planes will be discovered.</p>
<p><strong>The following fields are no longer used by the Kiali CR and MUST be removed, if currently set.</strong></p>
<ul>
<li><code>spec.external_services.istio.root_namespace</code></li>
</ul>
<h2 id="2150">2.15.0</h2>
<p>Release: September 02, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6041">Ambient: Improvements to Ambient workload validation</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8607">CI: Run all cypress tests from tags</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8659">CI: Add tests for kiali server/operator helm-charts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8681">CI: Validate CRDs are synced during release</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8632">Deployment: Add support for &ldquo;local&rdquo; mode</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8237">Deployment: Provide a schema for the Kiali CRD</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8606">Deployment: Support multiple control planes in different namespaces on the same cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8643">Operator: provide a way to verify operator permissions are correct</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8394">Perf: Only cache ConfigMaps in namespaces with controlplanes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8578">Perses: Add support for Perses Dashboard</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8657">Ambient: fix startup OOM in ambient environments</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8621">Operator: operator-sdk is now gone - operator release needs another way to verify bundle</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8639">Operator: missing permission in CSV for OLM installs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8648">UI: Multicluster Workload Validations icon padding</a></li>
</ul>
<h4 id="upgrade-change-notes-6">Upgrade Change Notes:</h4>
<p>Version 2.15.0 introduces a CRD schema for Kiali. The CRD version has not changed. But, validation will now occur on the cluster when the Kiali CRs are created or modified.</p>
<h2 id="2140">2.14.0</h2>
<p>Release: August 08, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7901">Ambient: UI support to add namespace to Ambient mesh</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8470">Deployment: Support for external kiali deployment option</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8272">Gateway API: Upgrade K8s Gateway API to v1.3.0</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8555">Gateway API: Support Gateway API Inference Extension</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8585">Authorization: do not perform cluster-wide query when cluster wide access is disabled</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8553">Multi-cluster: Detect monitoring port for each controlplane</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8590">Validation: Kiali does not recognize <code>istio-remote</code> gateway class</a></li>
</ul>
<h4 id="upgrade-change-notes-7">Upgrade Change Notes:</h4>
<p><strong>The following fields are no longer used by the Kiali CR and MUST be removed, if currently set.</strong></p>
<ul>
<li>no longer used
<ul>
<li><code>spec.istio_namespace</code></li>
<li><code>spec.in_cluster</code></li>
<li><code>spec.deployment.remote_secret_path</code></li>
</ul>
</li>
<li>now auto-discovered
<ul>
<li><code>spec.external_services.istio.config_map_name</code></li>
<li><code>spec.external_services.istio.istiod_pod_monitoring_port</code></li>
<li><code>spec.external_services.istio.envoy_admin_local_port</code></li>
<li><code>spec.external_services.istio.istio_canary_version</code></li>
<li><code>spec.external_services.istio.istio_injection_annotation</code></li>
<li><code>spec.external_services.istio.istio_sidecar_annotation</code></li>
<li><code>spec.external_services.istio.istiod_deployment_name</code></li>
<li><code>spec.external_services.istio.istiod_pod_monitoring_port</code></li>
<li><code>spec.external_services.istio.url_service_version</code></li>
</ul>
</li>
</ul>
<h2 id="2130">2.13.0</h2>
<p>Release: July 21, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/pull/8567">I18N: Spanish localization (partial)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8555">Istio Config: Initial support for GW API Inference extension</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8493">Mesh Page: Unify config format</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8552">Mesh Page: Consistent istio Metrics</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/pull/8573">MeshPage: Fix dataplane namespace count</a></li>
</ul>
<h2 id="2120">2.12.0</h2>
<p>Release: Jun 30, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8347">Usability: Cleanup logs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8349">Usability: Easy configuration/export of diagnostics</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7066">Usability: Show json logs in a more human readable format</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8345">Usability: Improve diagnostics for measuring performance</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8472">Usability: Improve tracing tool</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8491">Helm: be able to tell helm to skip creation of some resources</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8507">Operator: Adapt bundle CSV to FBC</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8517">Tracing: Be able to change the Trace limit default</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8527">Molecule: try to workaround another transient ansible galaxy error</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8531">Kiali.io: Features update</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8503">CI: Grafana Test Flake in OSSMC</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8518">CI: Shared Mesh page flaky test</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8528">CI: Add test coverage for the tracing tool</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8494">Tracing: Improve coverage when auth is specified but not required</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8505">Operator: change of kiali version produces error in op logs</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/455">OSSMC (CI): Adapt OSSMC cypress tests to OCP 4.19</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8495">OSSMC (CI): Cannot create property &lsquo;url&rsquo; on string &lsquo;GET&rsquo;</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8540">OSSMC (CI): failure in Workload logs tab</a></li>
</ul>
<h2 id="2110">2.11.0</h2>
<p>Release: Jun 09, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8338">Ambient: Support for ingress-use-waypoint</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7760">Grafana: support datasource_uid parameter for Grafana dashboards links</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8248">Istio: Support merging of multiple Istio configmaps</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8358">Kiali.io: document how to test a remote cluster secret / kubeconfig</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8449">Kiali.io: document how to use Kiali diagnostics for measuring performance</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8459">Operator: Refactor to not use kubernetes.core.k8s_cluster_info task</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8396">Perf: Remove Endpoints caching</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8361">Tracing: Mesh page &ldquo;Check Status&rdquo; option to help troubleshooting</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8348">Usability: Improve Kiali Logs and metrics for timing of a request</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8464">Ambient: Mode detection fix - DaemonSet filtering label matching assumes exact map match, uses wrong source of data</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8480">Ambient: Fix runtime error starting Kiali outside the cluster with Istio Ambient</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8442">UI: Show GW API Icon for GWs in the graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8478">UI: Fix internal server error when editing a workload</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8458">Usability: Fix missing Kiali metrics</a></li>
</ul>
<h2 id="2100">2.10.0</h2>
<p>Release: May 18, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7996">Ambient: Include ztunnel table filters</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8355">Code: Adopt controller-runtime client</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8373">Code: Adopt github.com/go-jose/go-jose/v3 instead of github.com/go-jose/go-jose</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8220">Gateway API: Load all k8s gateway API classes that use Istio as a controller</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5043">Kiali.io: Document features that enable you to more easily view a large graph</a></li>
<li><a href="https://github.com/kiali/kiali/pull/8330">Mesh Page: Load user config, if configured, and show on mesh page for istiod</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8346">Support: Add structured logging</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8317">Validation: Allow disabling validations</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8381">Ambient: Error Unmarshalling the config_dump in Istio Ambient 1.26</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8376">Build: Not able to build v1.73 integration test image + runtime GLIBC error from <code>oc</code></a></li>
<li><a href="https://github.com/kiali/kiali/issues/8417">OSSMC: Trying to show traffic animation in OpenShift console leads to error</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8406">Tempo: Does not return traces with error</a></li>
</ul>
<h2 id="290">2.9.0</h2>
<p>Release: Apr 25, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7830">CI: Use the sail operator instead of istioctl to deploy istio</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8097">CI: Update primary-remote (multicluster) pipeline to use Sail Operator</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8098">CI: Update external control plane pipeline to use Sail Operator</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8289">CI: Update workflows /test-istio-version.yml to use sail operator</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8314">Kiali.io: document the features that are supported by the operator but not by the server helm chart</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8315">Operator: Allow providing extra labels for server and operator</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8344">UI: Add &ldquo;Manual&rdquo; refresh interval</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8197">UI: Scroll in tables with sticky headers</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6357">Demos: Service Spawner demo not generating traffic </a></li>
<li><a href="https://github.com/kiali/kiali/issues/8007">Perf: Kiali uses a lot of CPU (in validations)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8304">Perf: Mesh page hangs for a long time when a component status is unhealthy</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8259">Server: Kiali not working when Istio native sidecars feature is disabled</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8284">Server: Difference in Istio and Kiali Workload Name for Argo Rollouts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8321">Operator: defining an inaccessible cluster in Kiali CR breaks the operator</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8258">UI: Node selection not working when navigating to graph from trace detail</a></li>
</ul>
<h2 id="280">2.8.0</h2>
<p>Release: Apr 07, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8024">Ambient: Include ztunnel specific metrics</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7952">Hack scripts: Support for auto-injection-label in all install scripts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8196">Mesh page: Include Kiali resource metrics in side-panel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6941">Operator: Watch for changes to remote cluster secrets</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7904">OSSMC: Integrate console tracing  with Kiali plugin</a></li>
<li><a href="https://github.com/kiali/kiali/pull/8277">Perf: Ambient graph generation optimization</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8211">Perf: Validation MultiMatchChecker optimization</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8210">Perf: Validation VirtualServices SubsetPresenceChecker optimization</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7877">Security: Use multi-cluster secret if it exists in the namespace</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7724">UI: Enhance masthead Istio Status with multi-cluster support and improved UX</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8154">UI: Workload detail Pod listing now shows the revision annotation</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8203">Health: Service Health calculation wrongly</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8189">Health: Ambient Inconsistency of Service Health between pages</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8271">K8s Gateway: API CRD check improvement</a></li>
</ul>
<p>Deprecations:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8053">Remove Cytoscape graph implementation</a></li>
</ul>
<p>After a 4 month deprecation period the support for Kiali&rsquo;s original, Cytoscape-based, graph implementation has ended.
The &lsquo;spec.kiali_feature_flags.ui_defaults.graph.impl&rsquo; configuration setting is no longer supported, and the sole
implementation going forward uses PatternFly Topology. This has allowed for a significant cleanup of the Kiali
code base, and removal of several dated dependencies. We&rsquo;d like to thank the <a href="https://cytoscape.org/">Cytoscape project</a>,
without which Kiali would not have existed. It is an excellent library, and our migration to PatternFly was motivated
by a need to settle on a uniform component library.</p>
<h2 id="270">2.7.0</h2>
<p>Release: Mar 17, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8145">Ambient: Add metrics to ztunnel tab for workload detail</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8144">Ambient: Add ztunnel resource consumption metrics to Mesh page side panel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8007">Perf: Validation and other perf enhancements</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6641">Code: Fix data race in GetKialiTokenForHomeCluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8232">Graph: PFT graph find/hide broken for &ldquo;label:&rdquo; operand</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8139">Validation: Inconsistency between Service list validation and service details</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8228">Validation: Service Details Config Validations Inconsistency</a></li>
</ul>
<h2 id="260">2.6.0</h2>
<p>Release: Feb 21, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7899">Ambient: Waypoint proxy log improvement</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8143">Ambient: Add ztunnel to mesh topology</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8050">Ambient: Recognize any gateway as a Waypoint if &ldquo;waypoint&rdquo; is in the name</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7603">Config: Allow mixed app and verion labeling schemes</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8146">Ambient: No ztunnel logs with waypoint in Istio 1.23</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8157">Ambient: Some Waypoint proxies are reported incorrectly</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8084">Authz: Fix access to DeploymentConfig (and some others)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8133">GW API: Wrong ReferenceGrant apiVersion from Kiali server</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7909">Logging: Istio sidecar logs missing with k8s native sidecar enabled</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8159">Mesh page: side panel does not stay in sync with mesh graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8100">Perf: Jaeger version check leads to delayed Kiali login screen until timeout occur</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8112">Tracing: Spans missing References values when Tempo is used</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8106">Tracing: Kiali does not report trace connectivity error</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8172">UI: Istio-system applications shown as out of mesh</a></li>
</ul>
<p>Upgrade Notes:</p>
<p>The default values for the following Kiali CR fields have changed:</p>
<ul>
<li>spec.istio_labels.app_label_name
<ul>
<li>previous default: &ldquo;app&rdquo;</li>
<li>new default:      unset</li>
</ul>
</li>
<li>spec.istio_labels.version_label_name
<ul>
<li>previous default: &ldquo;version&rdquo;</li>
<li>new default:      unset</li>
</ul>
</li>
</ul>
<p>The change is related to the work done for <a href="https://github.com/kiali/kiali/issues/7603">Kiali issue 7603</a>, included with this release. By default Kiali now allows for a mixing app labeling schemes, using the same set of app and version label pairings recognized by Istio:</p>
<ul>
<li>service.istio.io/canonical-name, service.istio.io/canonical-revision</li>
<li>app.kubernetes.io/name, app.kubernetes.io/version</li>
<li>app, version</li>
</ul>
<p>Users can configure a single labeling scheme by setting the existing CR fields, or leaving them set when upgrading.</p>
<h2 id="250">2.5.0</h2>
<p>Release: Feb 03, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/5979">Ambient: Trace support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7107">Istio: Workload Entry and Workload Group support for VMs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8058">Istio: WorkloadGroup Validations</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8054">Mesh Page: visualize gateways and waypoints</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7925">Multicluster: When login to remote cluster fails, no visible error appears</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5614">Operator: Add topologySpreadConstraints</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8057">Security: configure /api endpoint to require authentication</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8075">Istio: show configurations for K8sGateways</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8033">Ambient: Error reading logs when user doesn&rsquo;t have permissions for ztunnel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8101">Misc: Fix mixed object references with the same name for k8s gw</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8081">Multicluster: Error namespace not found in Multi Cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8069">UI: Fix color-scheme cached value handling</a></li>
</ul>
<h2 id="240">2.4.0</h2>
<p>Release: Jan 13, 2025</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7999">Ambient: Improve waypoint visualization</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7107">Config: Support Workload Group workload in list view</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7932">Misc: Formally support previous versions of Istio in Kiali releases</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7902">Misc: dual stack ipv6 support</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/8023">Operator: when on openshift, if ingress is disabled, skip some things that require the Route and abort if using openshift auth strategy</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7997">Tracing: GRPC Jaeger client using old tag for istio multi cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8036">Tracing: Tempo Version url doesn&rsquo;t work with TLS</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8034">UI: Workload Traffic tab navigation leaves Overview tab confused</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8025">UI: Irregular metrics loading error </a></li>
</ul>
<h2 id="230">2.3.0</h2>
<p>Release: Dec 23, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/pull/7970">Ambient - Several troubleshooting additions</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7977">Maintenance - Go version 1.23.2</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7769">Tempo - Performance review and cache introduced</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7934">Traffic Graph - New &ldquo;point-style&rdquo; traffic animation</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8004">UI - Show dual stack IPs in service details</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7937">Traffic graph - In ambient mode, graph missed some gateway traffic</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7958">UI - Kiosk mode Time duration component does not handle the URL correctly</a></li>
<li><a href="https://github.com/kiali/kiali/issues/8000">Validations - KIA1104 should only show when there is one route destination but has explicit weight assigned and less than 100 on tcp/tls route</a></li>
</ul>
<h2 id="220">2.2.0</h2>
<p>Release: Dec 02, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7820">Core, UI - Alternative Workload controllers support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7926">Multicluster - Pull the CA from the cluster and add that to the remote secret</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7832">Operator, Core - Adjustable readiness and liveness probes delay</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7922">Operator, Multicluster - allow multiple Kiali Servers in the same cluster each have cluster-wide-access enabled</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7903">Tempo - Optimize Tempo query</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7929">UI - Enable the Selection-based zoom in PFT</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7882">Validation, UI - Make gateways optional in istio status</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7935">UI - Traffic graph Zoomed-in &ldquo;reset view&rdquo; not resizing correctly</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7940">UI - Workload detail missing envoy tab when Istio working with native sidecars</a></li>
</ul>
<h2 id="210">2.1.0</h2>
<p>Release: Nov 11, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7623">Mesh Page - Consistent display format for configuration values on the Mesh page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7726">Mesh Page - Canary upgrade status only uses home cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7841">Operator - Operator should look for OpenShiftAPIServer to determine if its running on OCP</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7856">Operator - Bump base image to 4.17 / 1.35.0</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7896">Security - Move base image of Kiali Server to UBI9 / RHEL9</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7457">UI - Config list items should properly use Group + Version + Kind for kube resources</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7317">UI - Improve color choice for &ldquo;Not Ready&rdquo; icon in dark-mode</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7875">Ambient - External service shown as unknown</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7843">Ambient - When the graph nodes are inaccesible, the graph has duplicated edges (From L4 and L7)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7811">Ambient - Kiali doesn&rsquo;t show connection from ambient to sidecar injected namespace as mTLS</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7844">Mesh Page - Failed to get istio deployment status when using IP in external services URLs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7839">Minigraph - Unable to navigate between workloads using the minigraph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7878">Traffic Graph - Graph hide can leave orphan edges</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7802">Traffic Graph - PFT graph page throws a console error when the user navigates to the graph from a details page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7452">UI - Config list items must include apiVersion value when the Istio object is created outside of Kiali</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7690">Validation - Istio validations inconsisteny - exported to other namespace</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7789">Validation - Kiali states pod has no Istio sidecar under Workloads even though Istio has native sidecar support enabled</a></li>
</ul>
<p>Deprecations:</p>
<ul>
<li>RedHat Community Operator
<ul>
<li>The community operator created confusion as to which operator to use on OpenShift. It will no longer be updated and will eventually be
removed. OpenShift users are encouraged to use the productized operator, which is included with licensed copies of OpenShift.</li>
</ul>
</li>
</ul>
<h2 id="200">2.0.0</h2>
<p>Release: Oct 21, 2024</p>
<p>The first major Kiali release in over 5 years!  There are two main reasons for the major version update:</p>
<ol>
<li>There is a breaking change in Kiali&rsquo;s namespace management configuration. To limit the namespaces accessible to Kiali, or made visible to users, Kiali v2.0 users will configure Discovery Selectors.</li>
</ol>
<p>There is no longer support for the following deprecated configuration settings:</p>
<ul>
<li>spec.deployment.accessible_namespaces</li>
<li>api.namespaces.exclude</li>
<li>api.namespaces.include</li>
<li>api.namespaces.label_selector_exclude</li>
<li>api.namespaces.label_selector_include</li>
</ul>
<ol start="2">
<li>Kiali has a new traffic graph implementation.</li>
</ol>
<p>The Cytoscape implementation has been deprecated and is no longer the default. Kiali has moved to PatternFly Topology to align with the rest of the Kiali interface, which is already implemented using PatternFly components.  The old graph implementation will be removed as soon as the Kiali maintainers believe the new implementation has proven itself in the field. Until that time, it can still be accessed by setting:</p>
<div class="highlight"><pre tabindex="0" style="background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4;"><code class="language-yaml" data-lang="yaml"><span style="display:flex;"><span><span style="color:#204a87;font-weight:bold">spec</span><span style="color:#000;font-weight:bold">:</span><span style="color:#f8f8f8;text-decoration:underline">
</span></span></span><span style="display:flex;"><span><span style="color:#f8f8f8;text-decoration:underline">  </span><span style="color:#204a87;font-weight:bold">kiali_feature_flags</span><span style="color:#000;font-weight:bold">:</span><span style="color:#f8f8f8;text-decoration:underline">
</span></span></span><span style="display:flex;"><span><span style="color:#f8f8f8;text-decoration:underline">    </span><span style="color:#204a87;font-weight:bold">ui_defaults</span><span style="color:#000;font-weight:bold">:</span><span style="color:#f8f8f8;text-decoration:underline">
</span></span></span><span style="display:flex;"><span><span style="color:#f8f8f8;text-decoration:underline">      </span><span style="color:#204a87;font-weight:bold">graph</span><span style="color:#000;font-weight:bold">:</span><span style="color:#f8f8f8;text-decoration:underline">
</span></span></span><span style="display:flex;"><span><span style="color:#f8f8f8;text-decoration:underline">        </span><span style="color:#204a87;font-weight:bold">impl</span><span style="color:#000;font-weight:bold">:</span><span style="color:#f8f8f8;text-decoration:underline"> </span><span style="color:#4e9a06">&#34;cy&#34;</span><span style="color:#f8f8f8;text-decoration:underline">
</span></span></span></code></pre></div><p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7445">Ambient Graph - Improve Ambient Graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6900">Ambient Graph - Better visualize ztunnel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7702">Ambient Graph - Treat waypoint nodes as workloads, not apps</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7706">Ambient Graph - Use bidirectional edges between workloads and waypoints</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7546">Configuration - Discovery Selectors, enhance namespace accessibility per Discovery KEP</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7745">Configuration - change names of url / in_cluster_url to better reflect what they are</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7177">Configuration - Auto-detect more Istio config for ease-of-configuration</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7795">Configuration - Be able to specify auth.username and custom dashboards auth via secrets</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7569">Configuration - Support for additional environment variables in deployment</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7485">Extensions - Support 3rd party traffic metrics per Extensions KEP</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7814">Gateway API - K8s GW API v1.2.0 support</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/99">Graph - Patternfly topology for Kiali graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7515">Mesh Page - Improve istio canary handling</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7203">Mesh Page - Ensure per-control-plane Istio settings</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7058">Perf - Kiali Performance and Scalability testing</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7674">UI - Upgrade Patternfly to version 5.4</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7665">Kiali federation with multiple Kubernetes flavors not able to access none OpenShift workloads/applications when running on OCP</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7720">K8s Gateways: Out of mesh error when not in &lsquo;istio-system&rsquo;</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7717">bearer token auth with external Grafana</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7758">Config: grafana and tracing versions should be obtained over in_cluster_url</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7717">Auth: Fix issue with bearer token auth with external Grafana</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7758">Auth: Fix URL-choice issue when fetching Grafana and tracing versions</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7598">Mesh page - controlplanes not mapped to their dataplanes when using stable revision labels</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7598">Mesh page: Fix issue for controlplanes not mapped to their dataplanes, when using stable revision labels</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7441">Mesh page: Memory consumption chart for istiod container isn&rsquo;t getting created</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7829">Mesh page: istiod with no proxies synced yet throws error</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7665">Multicluster: Fix issue federating Kiali instances on different Kubernetes&rsquo; impls</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/375">OSSMC: Toggle menu of the workload minigraph does not load the action list</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7822">Tempo: View in Tracing link</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/375">UI: Toggle menu of the workload minigraph does not load the action list</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7817">UI: Broken Breadcrumb for Details pages</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7685">Validations - Inconsistency between List and Details pages</a></li>
</ul>
<h2 id="1894">1.89.4</h2>
<p>Release: Sep 30, 2024</p>
<p>Features:</p>
<p>The next feature release will be Kiali v 2.0.0</p>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7720">K8s Gateways: Fix &ldquo;Out of mesh&rdquo; error when not in &lsquo;istio-system&rsquo;</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7773">Operator: Fix support of namespaces that just have numbers in their name</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7685">Validations - Fix “exportTo” validation inconsistency between List and Detail pages</a></li>
</ul>
<h2 id="1893">1.89.3</h2>
<p>Release: Sep 09, 2024</p>
<p>Features:</p>
<p>The next feature release will be Kiali v 2.0.0</p>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7638">Custom Dashboard - External Links of Custom dashboard not visible</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7672">Graph - Cannot load the graph: cluster (unknown) is not found or is not accessible for Kiali</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7590">Graph - Inconsistent ServiceEntry Display in Multi-Namespace Environment</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7589">Graph - Fix handling of defaultExportTo setting in serviceEntry and other components</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7658">Tempo - query_scope is ignored for Tempo in single-cluster environment</a></li>
</ul>
<h2 id="1890">1.89.0</h2>
<p>Release: Aug 19, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7480">Maintenance - Upgrade go from 1.22.1 to 1.22.5</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7503">Maintenance - Move to node 20</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7527">Mesh page - Hide mesh page for non istio-system users</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7076">Perf - Kiali Performance improvements.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7553">UX - Align the notification badge with PF standards</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7542">Auth - k8s api token not auto refreshing for calls to fetch cacerts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7459">Mesh page - Display full yaml from <code>istio</code> configmap</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7619">Operator - when installing OSSMC, make sure the Kiali version is the same.</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/330">OSSMC - cannot update namespace or create Istio objects</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7622">OSSMC - Upgrade api from v1alpha1 to v1</a></li>
</ul>
<h2 id="1880">1.88.0</h2>
<p>Release: Jul 29, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7350">Ambient - Identify waypoint proxies for Istio Ambient</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7207">Dependencies - React Router migration from v5 to v6</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7527">Mesh page - Hide mesh page for non istio-system users</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7531">Mesh page - View Tempo version in Mesh Page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7501">K8s GW API - Autodiscover gateways</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7524">K8s GW API - Rework - Duplicate labels in Kiali CR and code</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7413">K8s GW API - Cross-Namespace routing</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/335">UI - Place alert notifications in the top right corner of the screen</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7553">UI - Align the notification badge with PF standards</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7475">Mesh page - Grafana version checks don&rsquo;t use configured Grafana auth</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7455">Mesh page - throws error when one of the clusters is inaccessible</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7332">Tracing - The tracing service is disabled by default</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7232">K8s GW API - Hardcoded ingressgateway labels in code</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7522">Cypress - KIA1102 validation fails - Issue in Kiali</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7549">Ambient - Hiding TCP hides HTTP</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7559">Kiali operator - helmchart frequently changes the replica count when HPA is enabled</a></li>
</ul>
<h2 id="1870">1.87.0</h2>
<p>Release: Jul 08, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7432">Ambient - Show Ambient labels in Service and Application details</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7473">Ambient - Improve Ambient appender performance</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7444">Graph - improve PFT &ldquo;focus node&rsquo;</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7355">K8s GW API - 1.1 Support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7223">K8s GW API - GRPCRoute support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7397">Kiali.io - Include performance results and improvements into kiali.io</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7490">Kiali.io - Add Kiali and Ambient documentation</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7476">Operator - ansible kubernetes.core collection update</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/317">OSSMC - Support for Gateway API objects in the Istio Config list page</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7448">Ambient - Cannot load the graph: Namespace is excluded</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7500">Ambient - ztunnel logs are using pod name (And not workload)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7504">Masthead - kiali may hang when asking for masthead&rsquo;s Debug Info while graph page is displayed</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7458">Mesh page - controlplanes have an edge to every dataplane</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7063">Multi-cluster - Visual bug on the Overview page upon refresh</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7447">Routing Wizard - Empty Matching fail</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7463">K8s GW API - ReferenceGrant has incorrect API version in the wizard</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/330">OSSMC cannot update namespace or create Istio objects</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7481">Validations - KIA0106 False Positive - Unable to Find Service Accounts</a></li>
</ul>
<p>Deprecations:</p>
<ul>
<li>Kiali is deprecating its current namespace selection approach. For a description of the new mechanism see <a href="https://github.com/kiali/kiali/blob/master/design/KEPS/namespace-discovery/proposal.md">https://github.com/kiali/kiali/blob/master/design/KEPS/namespace-discovery/proposal.md</a>. The following configuration is deprecated:
<ul>
<li>spec.deployment.accessible_namespaces</li>
</ul>
</li>
<li>Note that the following settings have already been deprecated and will soon be removed:
<ul>
<li>api.namespaces.exclude</li>
<li>api.namespaces.include</li>
<li>api.namespaces.label_selector_exclude</li>
<li>api.namespaces.label_selector_include</li>
</ul>
</li>
</ul>
<h2 id="1860">1.86.0</h2>
<p>Release: Jun 17, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7377">mesh page - Add legend to the mesh graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7379">mesh page = display side-panel JSON in a table format</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7344">ambient - support http ambient waypoint telemetry in graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7429">ambient - support http ambient waypoint telemetry in charts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7420">ambient - Adapt Auto Injection action in Ambient Mesh</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7388">Request for fetch traces is timeouted after 30s</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7394">Simplify i18n support </a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7384">Traces are not filtered for cluster in Multi cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7418">graph - PFT graph does not show parallel edges with different protocols</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7187">Helm chart/operator does not support Adding an Inaccessible Cluster </a></li>
<li><a href="https://github.com/kiali/kiali/issues/7256">CI - Flake - graph_context_menu nodes undefined</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7180">CI - Improve Cypress test related in kiali_help.feature</a></li>
</ul>
<h2 id="1850">1.85.0</h2>
<p>Release: May 27</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/5913">New Mesh Topology page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7266">Custom http headers for tracing</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7150">Add the ability to modify the dnsconfig for the kiali deployment in kubernetes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7238">make sure Kiali can observe important istiod metrics</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7357">kiali-server helm chart: Do not create ClusterRole if not needed</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/308">Include Mesh page in OSSMC</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7305">graph - Getting &ldquo;Cannot load the graph: cluster (kubernetes) is not found or is not accessible for Kiali&rdquo; with certain prometheus configurations.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6523">ambient - Improve check for detection of workload in Ambient Mesh</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7338">ambient - ztunnel logs are not shown on a kind cluster </a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/298">ossmc - Istio config list page does not filter by namespace (OCP 4.15)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6648">Vulnerability in Go Crypto CVE-2022-27191</a></li>
</ul>
<h2 id="1840">1.84.0</h2>
<p>Release: May 06, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6898">Ambient - support ztunnel access logs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7322">Operator - be able to disable namespace watching</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/198">OSSMC - Adapt OSSMC to PF5</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/279">OSSMC - Internationalization (I18N)</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7275">KIA1102 shows warning instead of a danger status</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/284">Traffic graph context menu options do not redirect to the correct pages</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7152">(multi-Cluster AuthorizationPolicy) (KIA0106) when namespace SPIFFY is on remote cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7287">False KIA1102 alert</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7315">Kiali fails to watch Gateway due to <code>spec.servers(*).tls.mode: OPTIONAL_MUTUAL</code> setting</a></li>
</ul>
<h2 id="1830">1.83.0</h2>
<p>Release: Apr 12, 2024</p>
<p>Features:</p>
<ul>
<li>n/a</li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7227">Namespace selector order is random</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/288">The Istio config list page does not update when switching from a forbidden namespace to an accessible one</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7252">token &amp; OpenShift authentication not working </a></li>
<li><a href="https://github.com/kiali/kiali/issues/7254">automaxprocs removed from kiali</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7259">Graph for Ambient ns is not generated correctly when the traffic is not generated throw a Gateway</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6777">(e2e) Tests should check status code before attempting to unmarshal into json</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7243">(molecule) flake in molecule test &ldquo;os-console-links-test&rdquo;</a></li>
</ul>
<h2 id="1820">1.82.0</h2>
<p>Release: Mar 22, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6036">Multicluster - External controlplane support</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6037">Multicluster - Token per cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7176">Tracing - Include a health_check_url for tracing external service</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7185">Tracing - Update Tempo resource usage</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6942">Auth - Enhancing Kiali OIDC process by supporting CSI secrets</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7086">Kiali tracing URLs don&rsquo;t work with Grafana 10+</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7127">Warning in workload &lsquo;istio-ingressgateway&rsquo; in non control-plane namespace</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7171">Distributed Tracing menu item active when there is no public URL defined</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7179">Graph - crash in DeadNode appender in multi mesh-setup</a></li>
</ul>
<h2 id="1810">1.81.0</h2>
<p>Release: Mar 01, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7093">Kiali Server Helm Chart Support Custom NodePort</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7071">envoy access log entry doc links are broken</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/251">Istio config href is broken</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/253">TLS information is not available</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/264">AlertUtils Kiali messages are not shown in OSSMC</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7145">Kiali operator does not preserve camel case on additional ingress labels</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7147">The duration label is confusing in the Overview control plane charts</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7149">Fix help text for graph Security Display option.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7153">(graph) ServiceEntry ExportTo is not handled correctly</a></li>
</ul>
<h2 id="1800">1.80.0</h2>
<p>Release: Feb 09, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6879">Make support of &ldquo;ExportTo&rdquo; feature of Istio config configurable</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6924">Use client-go&rsquo;s service account token client refresh</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7090">Kiali v1.73.x compatible with Istio 1.20 and GW API v1</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7089">Upgrade Patternfly to version 5.2</a></li>
<li><a href="https://github.com/kiali/kiali/issues/4597">Add pprof endpoints for debugging perf issues</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/7024">Multicluster - delete traffic routing on &ldquo;remote&rdquo; cluster 404</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/239">Switching namespaces does not work on Istio Config page</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7053">Error fetching Istio deployment status of the remote control plane in the Primary remote deployment</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7061">Validations: Missing KIA0005 in objects details page when wrongly exported</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7077">PFT Graph not handling graph background clicks</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7074">Close button on the Certificates information does not do anything</a></li>
</ul>
<h2 id="1790">1.79.0</h2>
<p>Release: Jan 19, 2024</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/5850">Tempo - Initial Support Complete</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6243">Multicluster - provide links to external Kialis without requiring istio secrets</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6937">Multicluster - Add documentation for configuring Kiali with primary-primary</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7025">K8s GW API - Support of TCP/TLS/GRPC Routes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6918">K8s GW API - Support of ReferenceGrant</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6966">Use the Prometheus <code>/-/healthy</code> endpoint for the default value for health_check_url</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7027">Ambient - Workload graph reports the istio-waypoint proxies as &ldquo;Out of Mesh&rdquo; </a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/192">re-enable ARM builds</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7030">Remove graph &ldquo;Compress-On-Hide&rdquo; Display option</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6677">Bug after v1.72.0 release with oAuth2 strategy when DisableRBAC is true</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7006">Potential runtime error in kube_cache.GetK8sGateways</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5734">Prometheus retention config not resolved correctly when using defaults in prom</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6946">Incorrect spacing and icon sizing in Graph Summary Panel</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6948">Istio config bug</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6950">kiali operator cannot determine kiali version when installing ossmc</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6955">Tracing client must use the Kiali SA Token (Not the user token)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6669">Double istio rev in configmap name</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6964">debug info shows incorrect log level</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6961">Fix rank options in the graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6971">Update axios HTTP client library</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6962">Kiali render hostnames as individual service instead of serviceentry as whole</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6982">Scrollbar in Workloads Logs view</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7000">UI Error after deleting Istio Config</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6998">Extra padding in long namespace names</a></li>
<li><a href="https://github.com/kiali/kiali/issues/7022">Graph: Link to App which does not exist</a></li>
</ul>
<h2 id="1780">1.78.0</h2>
<p>Release: Dec 08, 2023</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6768">Update Patternfly library to version 5.1</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6806">Add labels and annotations in wizards</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5692">Multicluster - When istiod is unavailable portforwarding requests scale with namespaces</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6432">Multicluster - Create an istio registry per primary</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6616">Tempo Integration - Use select for query in Tempo 2.2 </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6893">Apply new eslint rules only to edited files</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6888">(Kiali-operator Helm Chart) Mount /tmp instead of /tmp/ansible-operator/runner as emptyDir to enable read-only root filesystem</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6811">Workload logs - improve appearance of checkboxes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6912">Set Secure Attribute on Session Cookie </a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6773">Info icon in yaml editor&rsquo;s overview panel is not aligned properly</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6926">patternfly graph not showing node decorators</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6665">Kiali UI not showing API Docs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6780">(Multicluster) Not all reviews workloads are visible in Kiali </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6858">Integration tests - Kiali 1.73 is not compatible with Istio 1.20</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6856">Istio 1.20 incompatibility</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6870">Jaeger traces: Filter by percentile no returning any trace</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6881">tracing UI - hover over trace dots &ldquo;flickers&rdquo; the heat map</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6884">Health icon in Application summary panel graph looks weird</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6913">panic when observability section does not configure the tracing endpoint correctly</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6916">Show kiali own traces</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6911">Disalignment in API Documentation info for Workloads and Services</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5635">Link to trace does not always open trace details</a></li>
</ul>
<p>Deprecations:</p>
<ul>
<li>Kiali is deprecating use of the Jaeger exporter for Kiali&rsquo;s own traces. Kiali will move to supporting only the OTel exporter.</li>
</ul>
<h2 id="1770">1.77.0</h2>
<p>Release: Nov 17, 2023</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6795">Tempo - Wrong Distributed Tracing link for nav menu</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6540">Tempo - Span query returning emptly results </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6438">PF5 - Upgrade to patternfly 5</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6450">PF5 - Move table deprecated component</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6813">OSSMC - add version fields to operator CSV metadata for display in OS Console UI</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6704">helm-charts smoke test GH action fails to start</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6710">Traces are duplicated across both clusters </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6753">getNamespaceMetrics includes cluster in query params</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6792">(operator) only process one OSSMConsole CR</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6807">ossmc package.json did not get updated version during last build</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6787">empty tree entry in kiali.io installation menu and goes to incorrect place</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6714">Repeatedly refreshing causes the UI to crash</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6810">Extra space between left nav and top nav</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6815">Multicluster - Missing cluster param in Show traces</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6825">Trace link in Graph - Trace is not loaded when clicked</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6808">(run-kiali) Error fetching availability of the tracing service</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6847">Error deploying istio 1.20 with hack script in OpenShift</a></li>
</ul>
<h2 id="1760">1.76.0</h2>
<p>Release: Oct 27, 2023</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6716">Update go version 1.20.10</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6687">Tempo - Update the main external link to distributed tracing</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6689">Tempo - Update documentation</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6699">Tempo - Update Trace data on hover </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6742">Add cluster_name support for run-kiali.sh hack script</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6609">Istio warning/error status for situations where eastwestgateway is not healthy.</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6751">istio hack script: cluster name should not be set to empty string</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6706">OSSMC - build and release ossmc plugin at end of sprint</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/208">OSSMC - Add scrollbar environment variable</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6448">PF5 - Move deprecated component Dropdown</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6010">Kiali Crashing in sidecar validation (without a sidecar)</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6494">(CI) Test flake - workload logs</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6598">Unable to reach API Server &lsquo;istio APIs and resources are not present in cluster (Kubernetes)&rsquo;</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6772">Multi mesh setup results in an error when fetching workloads</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6669">Double istio rev in configmap name</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6674">Selecting a trace in the Graph does not mark the edges when using Tempo </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6682">Service of a remote app/workload is not reported in the detail view</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6693">Tempo - Incomplete span data</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6702">Invalid AuthorizationPolicy generated from Overview page </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6711">Envoy is duplicated across both clusters</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6712">Traffic tab in Apps details is duplicated for both clusters</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6738">(ci) need to fix CI script for running molecule tests on openshift</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6740">Gateway badge is not being applied to gateways in the graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6745">Inbound Metrics tab for the Service detail is duplicated for services in different clusters</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6750">setup-kind-ci.sh script fails if it is not executed from root folder</a></li>
</ul>
<h2 id="1750">1.75.0</h2>
<p>Release: Oct 06, 2023</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6429">GW API Multiple implementations</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6130">Support K8s native sidecars</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6449">PF5 Move deprecated Select</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5849">Tempo tempo reading traces</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6537">Tempo Rename to Tracing instead of Jaeger when applicable </a></li>
<li><a href="https://github.com/kiali/kiali/issues/6663">Tempo Update hack script to support OpenShift</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/203">Focus selector support in PF graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6522">Include Ambient annotations as configuration settings</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6599">FAQ on how to get Kiali and Istio versions</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6437">Remote cluster istio-system namespace card show data from primary control plane</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6510">&ldquo;Cannot load the graph: json: cannot unmarshal object into Go value of type ()*kubernetes.RegistryEndpoint&rdquo;</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6615">Multicluster - Traffic routings created via Graph page are always located in the local cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6632">Breadcrumb click on Istio Type filter - Filter type is reset</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6635">Grafana, Ingress, Egress pods not running in Openshift after installing istio via istioctl</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6633">K8sGateway Validations - Inconsistency in lists</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6639">Little disalignments in Kiali UI</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6657">Wrong cluster when double tapping on a service/application in node graph</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6670">molecule tests are broken due to upstream galaxy changes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6676">Annotation wizard behaviour is not correct when user add/deletes some annotations</a></li>
</ul>
<h2 id="1740">1.74.0</h2>
<p>Release: Sep 15, 2023</p>
<p>Features:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6429">Added support of multiple Gateway API classes</a></li>
<li><a href="https://github.com/kiali/kiali/issues/5848">Ensure Tempo works using jaeger-query</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6526">Update Releasing doc</a></li>
<li><a href="https://github.com/kiali/openshift-servicemesh-plugin/issues/202">Adjust PFT graph-tour</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6566">document minimum helm version</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6261">Make Kiali compatible with OSSMC</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6446">Minimal upgrade to PF5</a></li>
</ul>
<p>Fixes:</p>
<ul>
<li><a href="https://github.com/kiali/kiali/issues/6398">Duplicate test ID related to Overview page in Multicluster mode</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6458">PFGraph throws console error when hovering an application label</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6492">Graph not showing traffic from portals to travels in west cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6512">IstioType in istioconfigList is propagated to other views</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6535">kiali pod stay in Error status after node shutdown</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6544">Graph side-panel has multi-cluster issues</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6545">(make) work around opm render bug when building for OLM</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6548">Double tap on a node redirects to wrong cluster</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6561">UI issues in Graph replay for OSSMC</a></li>
<li><a href="https://github.com/kiali/kiali/issues/6504">Sorting by cluster does not work in the list view located in the Overview page</a></li>
</ul>

	<div class="text-muted mt-5 pt-3 border-top">
  Last modified September 11, 2026: <a href="https://github.com/kiali/kiali.io/commit/4c8e26a2e94aa65f705872e00c9357c8caa93674">Release Notes v2.32.0 (#1012) (4c8e26a)</a>
</div>

</div>


          </main>
        </div>
      </div>
      <footer class="td-footer row d-print-none">
  <div class="container-fluid">
    <div class="row mx-md-2">
      <div class="col-6 col-sm-4 text-xs-center order-sm-2">
        
        
        
<ul class="td-footer__links-list">
  
  <li class="td-footer__links-item" data-bs-toggle="tooltip" title="Kiali channel on Istio Slack" aria-label="Kiali channel on Istio Slack">
    <a target="_blank" rel="noopener" href="https://istio.slack.com/archives/CJVRXB09F" aria-label="Kiali channel on Istio Slack">
      <i class="fab fa-slack"></i>
    </a>
  </li>
  
  <li class="td-footer__links-item" data-bs-toggle="tooltip" title="Kiali on Twitter" aria-label="Kiali on Twitter">
    <a target="_blank" rel="noopener" href="https://twitter.com/kialiproject" aria-label="Kiali on Twitter">
      <i class="fab fa-twitter"></i>
    </a>
  </li>
  
  <li class="td-footer__links-item" data-bs-toggle="tooltip" title="Kiali on Medium" aria-label="Kiali on Medium">
    <a target="_blank" rel="noopener" href="https://medium.com/kialiproject" aria-label="Kiali on Medium">
      <i class="fab fa-medium-m"></i>
    </a>
  </li>
  
  <li class="td-footer__links-item" data-bs-toggle="tooltip" title="Kiali channel on YouTube" aria-label="Kiali channel on YouTube">
    <a target="_blank" rel="noopener" href="https://www.youtube.com/channel/UCcm2NzDN_UCZKk2yYmOpc5w" aria-label="Kiali channel on YouTube">
      <i class="fab fa-youtube"></i>
    </a>
  </li>
  
  <li class="td-footer__links-item" data-bs-toggle="tooltip" title="Kiali community calendar" aria-label="Kiali community calendar">
    <a target="_blank" rel="noopener" href="https://bit.ly/kiali-calendar" aria-label="Kiali community calendar">
      <i class="fas fa-calendar"></i>
    </a>
  </li>
  
</ul>

        
        
      </div>
      <div class="col-6 col-sm-4 text-end text-xs-center order-sm-3">
        
        
        
<ul class="td-footer__links-list">
  
  <li class="td-footer__links-item" data-bs-toggle="tooltip" title="Kiali on Github" aria-label="Kiali on Github">
    <a target="_blank" rel="noopener" href="https://github.com/kiali" aria-label="Kiali on Github">
      <i class="fab fa-github"></i>
    </a>
  </li>
  
</ul>

        
        
      </div>
      <div class="td-footer__copyright-etc col-12 col-sm-4 text-center py-2 order-sm-2">
        
        
        
      </div>
    </div>
  </div>
</footer>
    </div>
    
  <script src="/js/main.min.4c98e4e5de11af0c57e343f7a7f3151032b3e93f76a9a6d4ca35aae14d867ea5.js" integrity="sha256-TJjk5d4RrwxX40P3p/MVEDKz6T92qabUyjWq4U2GfqU=" crossorigin="anonymous"></script>
<script defer src="/js/click-to-copy.min.f724d3de49218995223b7316aa2e53e2b34bf42026bf399ebb21bb02212402d1.js" integrity="sha256-9yTT3kkhiZUiO3MWqi5T4rNL9CAmvzmeuyG7AiEkAtE=" crossorigin="anonymous"></script>
<script src='/js/tabpane-persist.js'></script>

  
<script async id="netlify-rum-container" src="/.netlify/scripts/rum" data-netlify-rum-site-id="05b3eed1-6ea2-41a1-8b64-c76bda241be6" data-netlify-deploy-branch="current" data-netlify-deploy-context="production" data-netlify-cwv-token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzaXRlX2lkIjoiMDViM2VlZDEtNmVhMi00MWExLThiNjQtYzc2YmRhMjQxYmU2IiwiYWNjb3VudF9pZCI6IjVkYzIyMmYwMDU5NGFiMDE4NzcwMTlmMyIsImRlcGxveV9pZCI6IjZhYTdmNTkzMDE0YzU1MDAwODYxN2U0NyIsImlzc3VlciI6Im5mc2VydmVyIn0.fWSrC8Dm0wsDVwL9xPKCHqOzR8EiQTjzzksbdOuDOeM"></script>
</body>
</html>