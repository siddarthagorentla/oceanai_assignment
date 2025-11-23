<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Autonomous QA Agent - Documentation</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
            line-height: 1.6;
            color: #24292f;
            max-width: 896px;
            margin: 0 auto;
            padding: 32px;
            background-color: #ffffff;
        }

        h1, h2, h3, h4, h5, h6 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }

        h1 {
            font-size: 2em;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 0.3em;
        }

        h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #d0d7de;
            padding-bottom: 0.3em;
        }

        h3 {
            font-size: 1.25em;
        }

        p {
            margin-top: 0;
            margin-bottom: 16px;
        }

        a {
            color: #0969da;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        ul, ol {
            padding-left: 2em;
            margin-top: 0;
            margin-bottom: 16px;
        }

        code {
            padding: 0.2em 0.4em;
            margin: 0;
            font-size: 85%;
            background-color: #afb8c133;
            border-radius: 6px;
            font-family: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, "Liberation Mono", monospace;
        }

        pre {
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
            background-color: #f6f8fa;
            border-radius: 6px;
        }

        pre code {
            background-color: transparent;
            padding: 0;
            font-size: 100%;
            word-break: normal;
            white-space: pre;
        }

        table {
            border-spacing: 0;
            border-collapse: collapse;
            width: 100%;
            margin-top: 0;
            margin-bottom: 16px;
        }

        table th, table td {
            padding: 6px 13px;
            border: 1px solid #d0d7de;
        }

        table th {
            font-weight: 600;
            background-color: #f6f8fa;
        }

        table tr:nth-child(2n) {
            background-color: #f6f8fa;
        }

        blockquote {
            padding: 0 1em;
            color: #57606a;
            border-left: 0.25em solid #d0d7de;
            margin: 0 0 16px 0;
        }

        .center-block {
            text-align: center;
        }
        
        .badges img {
            margin: 0 4px;
        }

        .nav-links {
            margin-bottom: 32px;
        }
    </style>
</head>
<body>

    <h1>🤖 Autonomous QA Agent for Test Case & Script Generation</h1>

    <div class="center-block">
        <div class="badges">
            <img src="https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
            <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
            <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
            <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
        </div>

        <p><strong>Build a "Testing Brain" that turns documentation into executable code.</strong></p>

        <p class="nav-links">
            <a href="#overview">Overview</a> • 
            <a href="#features">Features</a> • 
            <a href="#setup-instructions">Installation</a> • 
            <a href="#workflow">Usage</a> • 
            <a href="#project-structure">Structure</a> • 
            <a href="#contributing">Contributing</a>
        </p>
    </div>

    <hr>

    <h2 id="overview">📘 Overview</h2>
    <p>The <strong>Autonomous QA Agent</strong> is an intelligent testing system designed to streamline the Quality Assurance process. By utilizing a <strong>Retrieval-Augmented Generation (RAG)</strong> pipeline, this tool ingests your project documentation and HTML files to build a context-aware "testing brain."</p>
    <p>Unlike generic AI tools, this agent generates <strong>grounded</strong> positive/negative test cases and <strong>runnable Selenium Python scripts</strong> based strictly on your provided assets—ensuring zero hallucinations and high relevance to your actual codebase.</p>

    <h2 id="features">✨ Features</h2>
    <table>
        <thead>
            <tr>
                <th>Feature</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>📂 Knowledge Base Ingestion</strong></td>
                <td>Upload <code>.md</code>, <code>.txt</code>, <code>.json</code>, and <code>.html</code> files to construct a project-specific vector database.</td>
            </tr>
            <tr>
                <td><strong>🧪 Smart Test Case Generation</strong></td>
                <td>Automatically creates structured positive and negative test cases (Preconditions, Steps, Expected Results).</td>
            </tr>
            <tr>
                <td><strong>🤖 Selenium Script Creator</strong></td>
                <td>Converts selected test cases into fully executable Selenium Python scripts tailored to your DOM elements.</td>
            </tr>
            <tr>
                <td><strong>🧠 RAG-Powered Precision</strong></td>
                <td>Ensures all generated outputs are strictly tied to the uploaded documentation, eliminating AI hallucinations.</td>
            </tr>
        </tbody>
    </table>

    <h2 id="setup-instructions">🛠️ Setup Instructions</h2>

    <h3>Prerequisites</h3>
    <ul>
        <li><strong>Python 3.9+</strong></li>
        <li><strong>Google Chrome Browser</strong> (for Selenium execution)</li>
    </ul>

    <h3>Installation</h3>
    <ol>
        <li>
            <p><strong>Clone the repository</strong></p>
<pre><code>git clone &lt;your_repo_url&gt;
cd &lt;project_folder&gt;</code></pre>
        </li>
        <li>
            <p><strong>Install dependencies</strong></p>
<pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h2 id="running">▶️ Running the Application</h2>
    <p>The system consists of a FastAPI backend and a Streamlit frontend. You need to run both terminal sessions.</p>

    <h3>1. Start the Backend</h3>
    <p>Initialize the API server (RAG logic):</p>
<pre><code>uvicorn app.backend.main:app --reload --port 8000</code></pre>

    <h3>2. Start the Frontend</h3>
    <p>Launch the User Interface:</p>
<pre><code>streamlit run app/frontend/ui.py</code></pre>

    <h3>3. Access the UI</h3>
    <p>Open your browser and navigate to:</p>
    <blockquote>
        <p><a href="http://localhost:8501" target="_blank">http://localhost:8501</a></p>
    </blockquote>

    <h2 id="workflow">🔄 Workflow</h2>
    <ol>
        <li><strong>Upload Assets</strong><br>Navigate to the sidebar. Upload your <code>checkout.html</code> and any supporting documentation (e.g., requirements docs from the <code>assets/</code> folder).</li>
        <li><strong>Build Knowledge Base</strong><br>Click the <strong>"Process Files"</strong> button. The system will generate embeddings and store them in the vector database.</li>
        <li><strong>Generate Test Cases</strong><br>Go to the <strong>Test Case Agent</strong> tab. Enter a prompt based on your docs.<br><em>Example: "Generate test cases for discount code validation"</em></li>
        <li><strong>Generate Selenium Scripts</strong><br>Select a generated test case from the list and click <strong>"Generate Selenium Script"</strong>. The agent will output ready-to-run Python code.</li>
    </ol>

    <h2 id="examples">🧪 Examples</h2>

    <h3>Generated Test Case</h3>
    <p><strong>Title:</strong> Apply valid discount code</p>
    <ul>
        <li><strong>Preconditions:</strong>
            <ul>
                <li>User is on the checkout page.</li>
                <li>Cart contains at least one item.</li>
            </ul>
        </li>
        <li><strong>Steps:</strong>
            <ol>
                <li>Enter <code>"SAVE20"</code> in the discount field.</li>
                <li>Click the <strong>Apply</strong> button.</li>
            </ol>
        </li>
        <li><strong>Expected Result:</strong>
            <ul>
                <li>Total price reduces by 20%.</li>
                <li>Success message is displayed.</li>
            </ul>
        </li>
    </ul>

    <h3>Generated Selenium Script</h3>
<pre><code>from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Driver
driver = webdriver.Chrome()
driver.get("file:///path/to/checkout.html")

# Execute Steps
driver.find_element(By.ID, "coupon").send_keys("SAVE20")
driver.find_element(By.ID, "apply-btn").click()

# Assertions (Example)
time.sleep(2)
success_msg = driver.find_element(By.ID, "success-message").text
assert "applied" in success_msg

driver.quit()</code></pre>

    <h2 id="project-structure">📁 Project Structure</h2>
<pre><code>root/
├── app/
│   ├── backend/        # FastAPI app & RAG logic
│   └── frontend/       # Streamlit UI components
├── assets/             # Sample HTML + documentation for testing
├── data/               # Storage for uploaded files & vector DB
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation</code></pre>

    <h2 id="contributing">🤝 Contributing</h2>
    <p>Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are <strong>greatly appreciated</strong>.</p>
    <ol>
        <li>Fork the Project</li>
        <li>Create your Feature Branch (<code>git checkout -b feature/AmazingFeature</code>)</li>
        <li>Commit your Changes (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
        <li>Push to the Branch (<code>git push origin feature/AmazingFeature</code>)</li>
        <li>Open a Pull Request</li>
    </ol>

    <hr>

    <div class="center-block">
        <p>Made with ❤️ by [Your Name/Team]</p>
    </div>

</body>
</html>
