# 🤖 Autonomous QA Agent for Test Case & Script Generation

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

**Build a "Testing Brain" that turns documentation into executable code.**

[Overview](#-overview) • [Features](#-features) • [Installation](#-setup-instructions) • [Usage](#-workflow) • [Project Structure](#-project-structure) • [Contributing](#-contributing)

</div>

---

## 📘 Overview

The **Autonomous QA Agent** is an intelligent testing system designed to streamline the Quality Assurance process. By utilizing a **Retrieval-Augmented Generation (RAG)** pipeline, this tool ingests your project documentation and HTML files to build a context-aware "testing brain."

Unlike generic AI tools, this agent generates **grounded** positive/negative test cases and **runnable Selenium Python scripts** based strictly on your provided assets—ensuring zero hallucinations and high relevance to your actual codebase.

---

## ✨ Features

| Feature | Description |
| :--- | :--- |
| **📂 Knowledge Base Ingestion** | Upload `.md`, `.txt`, `.json`, and `.html` files to construct a project-specific vector database. |
| **🧪 Smart Test Case Generation** | Automatically creates structured positive and negative test cases (Preconditions, Steps, Expected Results). |
| **🤖 Selenium Script Creator** | Converts selected test cases into fully executable Selenium Python scripts tailored to your DOM elements. |
| **🧠 RAG-Powered Precision** | Ensures all generated outputs are strictly tied to the uploaded documentation, eliminating AI hallucinations. |

---

## 🛠️ Setup Instructions

### Prerequisites
*   **Python 3.9+**
*   **Google Chrome Browser** (for Selenium execution)

### Installation

1.  **Clone the repository**
    ```bash
    git clone <your_repo_url>
    cd <project_folder>
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Running the Application

The system consists of a FastAPI backend and a Streamlit frontend. You need to run both terminal sessions.

### 1. Start the Backend
Initialize the API server (RAG logic):
```bash
uvicorn app.backend.main:app --reload --port 8000

### 2. Start the Frontend
Launch the User Interface:

streamlit run app/frontend/ui.py

3. Access the UI
Open your browser and navigate to:
http://localhost:8501
🔄 Workflow
Upload Assets
Navigate to the sidebar. Upload your checkout.html and any supporting documentation (e.g., requirements docs from the assets/ folder).
Build Knowledge Base
Click the "Process Files" button. The system will generate embeddings and store them in the vector database.
Generate Test Cases
Go to the Test Case Agent tab. Enter a prompt based on your docs.
Example: "Generate test cases for discount code validation"
Generate Selenium Scripts
Select a generated test case from the list and click "Generate Selenium Script". The agent will output ready-to-run Python code.
🧪 Examples
Generated Test Case
Title: Apply valid discount code
Preconditions:
User is on the checkout page.
Cart contains at least one item.
Steps:
Enter "SAVE20" in the discount field.
Click the Apply button.
Expected Result:
Total price reduces by 20%.
Success message is displayed.
Generated Selenium Script
code
Python
from selenium import webdriver
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

driver.quit()
📁 Project Structure
code
Bash
root/
├── app/
│   ├── backend/        # FastAPI app & RAG logic
│   └── frontend/       # Streamlit UI components
├── assets/             # Sample HTML + documentation for testing
├── data/               # Storage for uploaded files & vector DB
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
<div align="center">
<p>Project by Siddartha Gorentla</p>
</div>
```
