

    @media(max-width:900px){.grid{grid-template-columns:1fr}.features{grid-template-columns:1fr}}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">QA</div>
      <div>
        <h1>Autonomous QA Agent — Test Case & Selenium Script Generation</h1>
        <p class="lead">An intelligent agent that builds a testing brain from project docs & HTML, then generates grounded test cases and runnable Selenium Python scripts using a RAG pipeline.</p>
        <div class="badges">
          <div class="badge">Python 3.9+</div>
          <div class="badge">FastAPI</div>
          <div class="badge">Streamlit</div>
          <div class="badge">Selenium</div>
          <div class="badge">RAG</div>
        </div>
      </div>
    </header>

    <div class="grid">
      <main class="card">
        <section class="section">
          <h2>Overview</h2>
          <p class="muted">This repo ingests documentation (.md, .txt, .json) and HTML to create a vector-backed knowledge base. It produces positive & negative test cases and converts them into executable Selenium scripts. Everything is grounded via Retrieval-Augmented Generation.</p>
        </section>

        <section class="section">
          <h2>Features</h2>
          <div class="features">
            <div class="feature">📘 <strong>Knowledge Base Ingestion</strong><div class="muted">Upload docs & HTML — embeddings stored in a vector DB</div></div>
            <div class="feature">🧪 <strong>Test Case Generation</strong><div class="muted">Positive & negative flows based on docs</div></div>
            <div class="feature">🤖 <strong>Selenium Script Generation</strong><div class="muted">One-click convert test case → runnable Python Selenium script</div></div>
            <div class="feature">🔎 <strong>RAG Pipeline</strong><div class="muted">Outputs are grounded in source documents to avoid hallucination</div></div>
          </div>
        </section>

        <section class="section">
          <h2>Quick Start</h2>
          <div class="tabs" role="tablist">
            <button class="tab active" data-target="#install">Install</button>
            <button class="tab" data-target="#run">Run</button>
            <button class="tab" data-target="#usage">Usage</button>
          </div>

          <div id="install" class="panel">
            <p class="muted"><strong>Prerequisites</strong>: Python 3.9+, Google Chrome (for Selenium).</p>
            <pre><code>git clone &lt;your_repo_url&gt;
cd &lt;project_folder&gt;
pip install -r requirements.txt</code></pre>
          </div>

          <div id="run" class="panel" style="display:none">
            <pre><code># Start Backend
uvicorn app.backend.main:app --reload --port 8000

# Start Frontend
streamlit run app/frontend/ui.py

# Open UI
http://localhost:8501</code></pre>
          </div>

          <div id="usage" class="panel" style="display:none">
            <ol>
              <li>Upload <code>checkout.html</code> and support docs via sidebar/upload.</li>
              <li>Click <em>Build Knowledge Base</em> to process files and create embeddings.</li>
              <li>Go to <strong>Test Case Agent</strong> → enter prompt (e.g., "Generate test cases for discount code").</li>
              <li>Select a test case & click <em>Generate Selenium Script</em>.</li>
            </ol>
          </div>
        </section>

        <section class="section">
          <h2>Project Structure</h2>
          <pre><code>app/
 ├── backend/      # FastAPI + RAG logic
 ├── frontend/     # Streamlit UI
assets/            # sample HTML & specs
data/              # uploaded files & vector database
</code></pre>
        </section>

        <section class="section">
          <h2>Example Outputs</h2>
          <div class="collapsible">
            <details>
              <summary>Test Case (Example)</summary>
              <pre><code>Title: Apply valid discount code
Pre-conditions: User on checkout page, cart contains items
Steps:
  1. Enter code 'SAVE20' in coupon field
  2. Click Apply
Expected: Total reduced by 20% and success message displayed
</code></pre>
            </details>

            <details>
              <summary>Selenium Script (Snippet)</summary>
              <pre><code>from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///path/to/checkout.html')
code_input = driver.find_element(By.ID, 'coupon')
code_input.send_keys('SAVE20')
driver.find_element(By.ID,'apply-btn').click()
# assert discount applied
</code></pre>
            </details>
          </div>
        </section>

        <section class="section">
          <h2>Contributing</h2>
          <p class="muted">PRs welcome. For major changes, open an issue first to discuss your plan and avoid duplicate work.</p>
        </section>

        <section class="section">
          <h2>License</h2>
          <p class="muted">MIT License — see <code>LICENSE</code> file.</p>
        </section>

        <section class="section">
          <h2>Extras</h2>
          <div class="actions">
            <button class="btn" id="downloadBtn">Download README.html</button>
            <button class="btn ghost" id="copyMd">Copy Markdown</button>
          </div>
        </section>

      </main>

      <aside class="card">
        <h3>Table of Contents</h3>
        <nav class="toc">
          <ul>
            <li><a href="#overview">Overview</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#quick-start">Quick Start</a></li>
            <li><a href="#project-structure">Project Structure</a></li>
            <li><a href="#examples">Example Outputs</a></li>
            <li><a href="#contributing">Contributing</a></li>
          </ul>
        </nav>

        <div style="margin-top:12px">
          <h4>Badges</h4>
          <div class="badges">
            <div class="badge">build: passing</div>
            <div class="badge">coverage: 92%</div>
            <div class="badge">license: MIT</div>
          </div>
        </div>

        <div style="margin-top:12px">
          <h4>Quick Commands</h4>
          <pre><code>pip install -r requirements.txt
uvicorn app.backend.main:app --reload</code></pre>
        </div>

        <div style="margin-top:12px">
          <h4>Authors</h4>
          <p class="muted">Your Team — Autonomous QA Agent</p>
        </div>
      </aside>
    </div>

    <footer>
      <div>Made with ⚙️ and ☕ — Autonomous QA Agent • <span class="muted">Generated README</span></div>
    </footer>
  </div>

  <script>
    // Tabs
    document.querySelectorAll('.tab').forEach(btn=>btn.addEventListener('click',()=>{
      document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
      btn.classList.add('active');
      document.querySelectorAll('.panel').forEach(p=>p.style.display='none');
      const target=document.querySelector(btn.dataset.target);
      if(target) target.style.display='block';
    }));

    // Download file
    document.getElementById('downloadBtn').addEventListener('click', ()=>{
      const blob = new Blob([document.documentElement.outerHTML], {type: 'text/html'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = 'README.html'; a.click();
      URL.revokeObjectURL(url);
    });

    // Copy placeholder markdown (simple conversion)
    document.getElementById('copyMd').addEventListener('click', async ()=>{
      const md = `# Autonomous QA Agent\n\nAn intelligent, autonomous QA agent that constructs a \"testing brain\" from project documentation and HTML structure.\n\n## Features\n- Knowledge Base Ingestion\n- Test Case Generation\n- Selenium Script Generation\n- RAG Pipeline\n\n## Quick Start\n...`;
      await navigator.clipboard.writeText(md);
      alert('Markdown copied to clipboard (short version).');
    });
  </script>
</body>
</html>

