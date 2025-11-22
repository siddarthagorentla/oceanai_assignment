<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Autonomous QA Agent — README</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--muted:#94a3b8;--accent:#06b6d4;--glass:rgba(255,255,255,0.03)}
    html,body{height:100%;margin:0;font-family:Inter,ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial}
    body{background:linear-gradient(180deg,#041024 0%, #071427 60%);color:#e6eef6;line-height:1.5}
    .container{max-width:980px;margin:28px auto;padding:28px;background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));border-radius:14px;box-shadow:0 6px 30px rgba(2,6,23,0.6)}
    header{display:flex;align-items:center;gap:18px}
    .logo{width:72px;height:72px;border-radius:12px;background:linear-gradient(135deg,#06b6d4,#7c3aed);display:flex;align-items:center;justify-content:center;font-weight:700;color:#021025;font-size:28px}
    h1{margin:0;font-size:28px}
    .subtitle{color:var(--muted);margin-top:6px}
    .badges{margin-top:14px;display:flex;gap:8px;flex-wrap:wrap}
    .grid{display:grid;grid-template-columns:1fr 320px;gap:18px;margin-top:22px}
    .card{background:var(--card);padding:18px;border-radius:12px}
    pre{background:var(--glass);padding:12px;border-radius:8px;overflow:auto;color:#cfeffd}
    code{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Roboto Mono,monospace}
    .muted{color:var(--muted)}
    details{background:linear-gradient(90deg, rgba(255,255,255,0.01), rgba(255,255,255,0.005));padding:12px;border-radius:8px}
    summary{cursor:pointer;font-weight:600}
    .cta{display:flex;gap:10px;margin-top:12px}
    .btn{background:transparent;border:1px solid rgba(255,255,255,0.06);padding:8px 12px;border-radius:8px;cursor:pointer}
    .primary{background:linear-gradient(90deg,#06b6d4,#7c3aed);border:none;color:#021025;font-weight:700}
    footer{margin-top:18px;color:var(--muted);font-size:13px}
    .copy-btn{float:right;background:transparent;border:none;color:var(--muted);cursor:pointer}
    @media(max-width:880px){.grid{grid-template-columns:1fr} .logo{width:56px;height:56px}}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">QA</div>
      <div>
        <h1>Autonomous QA Agent — README</h1>
        <div class="subtitle">Smart, RAG-powered test case & Selenium script generation — documentation-driven automation.</div>
        <div class="badges">
          <img src="https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python" alt="python"/>
          <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square&logo=fastapi" alt="fastapi"/>
          <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square&logo=streamlit" alt="streamlit"/>
          <img src="https://img.shields.io/badge/Selenium-Automation-43B02A?style=flat-square&logo=selenium" alt="selenium"/>
        </div>
      </div>
    </header>

    <div class="grid">
      <main>
        <section class="card">
          <h2>Overview</h2>
          <p class="muted">This project ingests your docs and HTML, builds an internal knowledge base, and generates reliable test cases plus runnable Selenium scripts using a RAG pipeline. Outputs are grounded in uploaded files — no hallucinations.</p>

          <h3 style="margin-top:16px">Features</h3>
          <ul>
            <li><strong>Knowledge Base Ingestion</strong> — MD, TXT, JSON, HTML &rarr; vector store.</li>
            <li><strong>Test Case Generation</strong> — Positive &amp; negative flows generated from docs.</li>
            <li><strong>Selenium Script Generation</strong> — Convert test cases to runnable Selenium Python scripts.</li>
            <li><strong>RAG Pipeline</strong> — Ensures outputs are document-grounded.</li>
          </ul>

          <h3 style="margin-top:12px">Quick Start</h3>
          <ol>
            <li>Clone the repo</li>
            <li>Install requirements: <code>pip install -r requirements.txt</code></li>
            <li>Start backend: <code>uvicorn app.backend.main:app --reload --port 8000</code></li>
            <li>Start frontend: <code>streamlit run app/frontend/ui.py</code></li>
            <li>Open <code>http://localhost:8501</code></li>
          </ol>

          <details open>
            <summary>Workflow (click to expand)</summary>
            <ol style="margin-top:8px">
              <li><strong>Upload Assets</strong> — upload <code>checkout.html</code> and support docs via the sidebar.</li>
              <li><strong>Build Knowledge Base</strong> — process files to create embeddings.</li>
              <li><strong>Generate Test Cases</strong> — use the Test Case Agent tab with prompts like "Generate test cases for discount code".</li>
              <li><strong>Generate Scripts</strong> — pick a test case and click "Generate Selenium Script".</li>
            </ol>
          </details>

          <h3 style="margin-top:12px">Project Structure</h3>
          <pre><code>app/
 ├── backend/
 │    ├── main.py           # FastAPI API server
 │    ├── rag_engine.py     # RAG logic
 │    └── utils/            # parsing + embedding helpers
 ├── frontend/
 │    └── ui.py             # Streamlit UI
 assets/                    # sample HTML + docs
 data/                      # uploaded files + vector DB
</code></pre>

          <h3 style="margin-top:12px">Example Outputs</h3>
          <ul>
            <li><strong>Test Cases:</strong> Structured title, preconditions, steps, expected results, positive &amp; negative flows.</li>
            <li><strong>Selenium Scripts:</strong> WebDriver setup, locators extracted, actions &amp; assertions — ready to run.</li>
          </ul>

        </section>

        <section class="card" style="margin-top:16px">
          <h2>Usage Examples</h2>
          <div style="position:relative">
            <button class="copy-btn" onclick="copySnippet('cli')">Copy</button>
            <pre id="cli"><code>git clone &lt;your_repo_url&gt;
cd &lt;project_name&gt;

pip install -r requirements.txt

# Start backend
uvicorn app.backend.main:app --reload --port 8000

# Start frontend
streamlit run app/frontend/ui.py

# Open http://localhost:8501</code></pre>
          </div>

          <h4 style="margin-top:12px">Sample prompt for test-case generation</h4>
          <pre><code>Generate test cases for discount code validation including:
- valid code (percentage)
- expired code
- invalid format
- minimum cart value not met</code></pre>
        </section>

        <section class="card" style="margin-top:16px">
          <h2>Contributing</h2>
          <p class="muted">Contributions welcome. Open an issue for significant changes before submitting a PR. Keep changes focused and include tests for new functionality.</p>

          <h3 style="margin-top:10px">Roadmap (optional)</h3>
          <ul>
            <li>Repository templates for different app types</li>
            <li>Prebuilt Selenium test templates</li>
            <li>CI integration (GitHub Actions) to run generated scripts</li>
            <li>Dockerized backend + frontend</li>
          </ul>
        </section>

      </main>

      <aside>
        <div class="card">
          <h3>Quick Links</h3>
          <p class="muted">Useful commands &amp; notes</p>
          <pre><code># Install
pip install -r requirements.txt

# Backend
uvicorn app.backend.main:app --reload --port 8000

# Frontend
streamlit run app/frontend/ui.py</code></pre>

          <div style="margin-top:10px">
            <button class="btn" onclick="document.getElementById('download').scrollIntoView({behavior:'smooth'})">Download README</button>
            <button class="btn primary" onclick="copyToClipboard(fullHtml)">Copy full HTML</button>
          </div>

          <hr style="margin:14px 0;border:none;border-top:1px solid rgba(255,255,255,0.03)"/>

          <h4>Requirements</h4>
          <ul class="muted">
            <li>Python 3.9+</li>
            <li>Chrome Browser (Selenium)</li>
          </ul>

          <h4 style="margin-top:10px">License</h4>
          <p class="muted">MIT License</p>
        </div>

        <div class="card" style="margin-top:14px">
          <h3>Badges</h3>
          <div class="badges">
            <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square"/>
            <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square"/>
          </div>
        </div>
      </aside>
    </div>

    <footer>
      <div id="download" style="margin-top:18px"></div>
      <small class="muted">Generated README — Autonomous QA Agent • &copy; 2025</small>
    </footer>
  </div>

  <script>
    const fullHtml = `<!doctype html>\n<html lang="en">\n<head>\n  <meta charset="utf-8" />\n  <meta name="viewport" content="width=device-width,initial-scale=1" />\n  <title>Autonomous QA Agent — README</title>\n</head>\n<body>\n  <!-- README content (same as displayed) -->\n</body>\n</html>`;

    function copySnippet(id){
      const el = document.getElementById(id);
      if(!el) return;
      navigator.clipboard.writeText(el.innerText).then(()=>{
        alert('Copied to clipboard');
      });
    }

    function copyToClipboard(text){
      navigator.clipboard.writeText(text).then(()=>{alert('Full HTML copied to clipboard')});
    }

    // make pre/code blocks selectable for copy
    document.querySelectorAll('pre code').forEach(block=>block.setAttribute('contenteditable', 'false'));
  </script>
</body>
</html>
