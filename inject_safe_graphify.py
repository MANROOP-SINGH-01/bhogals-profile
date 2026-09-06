import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Clean script injection that appends graphify section after preloader hides / DOM loaded
injection_script = '''
<script>
(function() {
  function injectGraphify() {
    if (document.getElementById('graphify')) return;
    const gamingSec = document.getElementById('gaming');
    if (!gamingSec) return;

    const graphSec = document.createElement('section');
    graphSec.id = 'graphify';
    graphSec.className = 'relative bg-transparent py-24 max-md:py-14 md:py-32';
    graphSec.innerHTML = `
      <div class="mx-auto max-w-[1400px] px-6 md:px-12">
        <div class="flex items-center gap-3 font-mono text-xs uppercase tracking-[0.3em] text-muted">
          <span class="text-accent font-bold">06</span>
          <span class="relative h-px w-10 overflow-hidden bg-border-strong text-accent" aria-hidden="true">
            <span class="eyebrow-scan absolute inset-y-0 left-0 w-2/5 bg-current"></span>
          </span>
          <span>Knowledge Architecture</span>
        </div>

        <div class="mt-4 flex flex-col gap-6 md:flex-row md:items-end md:justify-between">
          <div>
            <h2 class="max-w-xl text-3xl font-medium tracking-tighter text-foreground sm:text-4xl md:text-5xl">
              Interactive <span class="text-accent">Knowledge Graph</span>
            </h2>
            <p class="mt-2 max-w-2xl font-mono text-xs uppercase tracking-wider text-muted">
              Dynamic GraphRAG network architecture &bull; 3,011 nodes &bull; 8,812 edges &bull; 119 communities mapped
            </p>
          </div>
          <div class="flex items-center gap-3">
            <a href="/graphify-out/graph.html" target="_blank" rel="noreferrer"
               class="inline-flex items-center gap-2 rounded-full border border-accent/40 bg-accent/10 px-5 py-2.5 font-mono text-xs uppercase tracking-widest text-accent transition-all duration-200 hover:bg-accent hover:text-black hover:shadow-[0_0_20px_rgba(78,205,196,0.4)]">
              <svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                <path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
              Full Screen Graph
            </a>
          </div>
        </div>

        <div class="relative mt-8 overflow-hidden rounded-2xl border border-border-strong bg-[#0d0d16]/90 shadow-2xl backdrop-blur-xl">
          <div class="flex items-center justify-between border-b border-border-strong/60 bg-surface/50 px-6 py-3 font-mono text-[11px] text-muted">
            <div class="flex items-center gap-3">
              <span class="inline-block h-2 w-2 rounded-full bg-emerald-400 animate-pulse"></span>
              <span class="text-foreground tracking-wider uppercase">GRAPHIFY LIVE ENGINE</span>
              <span class="text-muted-dim">|</span>
              <span class="text-muted hidden sm:inline">VIS-NETWORK v9.1.6</span>
            </div>
            <div class="flex items-center gap-4 text-xs">
              <span class="text-accent">3,011 NODES</span>
              <span class="text-muted-dim">/</span>
              <span class="text-foreground">8,812 EDGES</span>
            </div>
          </div>

          <div class="relative w-full" style="height: 680px;">
            <iframe 
              src="/graphify-out/graph.html" 
              title="Graphify Interactive Knowledge Graph"
              class="w-full h-full border-0"
              loading="lazy">
            </iframe>
          </div>

          <div class="grid grid-cols-2 gap-4 border-t border-border-strong/60 bg-surface/30 px-6 py-4 font-mono text-xs sm:grid-cols-4">
            <div>
              <div class="text-[10px] uppercase tracking-widest text-muted">Nodes Extracted</div>
              <div class="text-sm font-semibold text-foreground">3,011 Symbols</div>
            </div>
            <div>
              <div class="text-[10px] uppercase tracking-widest text-muted">Cross Connections</div>
              <div class="text-sm font-semibold text-accent">8,812 Edges</div>
            </div>
            <div>
              <div class="text-[10px] uppercase tracking-widest text-muted">Louvain Communities</div>
              <div class="text-sm font-semibold text-foreground">119 Clusters</div>
            </div>
            <div>
              <div class="text-[10px] uppercase tracking-widest text-muted">Confidence Level</div>
              <div class="text-sm font-semibold text-emerald-400">90% Verified</div>
            </div>
          </div>
        </div>
      </div>
    `;

    gamingSec.parentNode.insertBefore(graphSec, gamingSec.nextSibling);

    // Also add nav link smoothly to header nav if exists
    const navUl = document.querySelector('nav ul');
    if (navUl && !document.getElementById('nav-graphify')) {
      const li = document.createElement('li');
      li.id = 'nav-graphify';
      li.innerHTML = '<a href="#graphify" class="relative font-mono text-[0.8rem] uppercase tracking-widest transition-colors duration-200 text-muted hover:text-accent"><span class="relative">Graphify</span></a>';
      const contactLi = navUl.querySelector('li:last-child');
      if (contactLi) {
        navUl.insertBefore(li, contactLi);
      } else {
        navUl.appendChild(li);
      }
    }
  }

  if (document.readyState === 'complete') {
    setTimeout(injectGraphify, 1000);
  } else {
    window.addEventListener('load', function() {
      setTimeout(injectGraphify, 1000);
    });
  }
})();
</script>
'''

if '</body>' in html:
    html = html.replace('</body>', injection_script + '\n</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Injected safe post-hydration script successfully!")
else:
    print("</body> not found")
