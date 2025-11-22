Autonomous QA Agent for Test Case and Script Generation

An autonomous QA system that builds a “testing brain” from project documentation and HTML files. It generates grounded test cases and runnable Selenium Python scripts using a Retrieval-Augmented Generation (RAG) pipeline.

📘 Overview

This project ingests documentation and HTML, converts them into embeddings, and uses them to generate:

Positive & negative test cases

Executable Selenium Python scripts

Everything is grounded in the provided documents — no hallucinations.

✨ Features

Knowledge Base Ingestion
Upload .md, .txt, .json, and .html files to build a vector database.

Test Case Generation
Automatically generate complete, structured positive and negative test cases.

Selenium Script Generation
Convert a chosen test case into a runnable Selenium script.

RAG Pipeline
Ensures all outputs remain tied to your actual project documentation.

🛠️ Setup Instructions
Prerequisites

Python 3.9+

Google Chrome Browser

Installation
git clone <your_repo_url>
cd <project_folder>
pip install -r requirements.txt

▶️ Running the Application

The app includes:

FastAPI backend

Streamlit frontend

1. Start the Backend
uvicorn app.backend.main:app --reload --port 8000

2. Start the Frontend
streamlit run app/frontend/ui.py

3. Access the UI

Open:

http://localhost:8501

🔄 Workflow

Upload Assets
Upload checkout.html and supporting documents from the assets/ folder.

Build Knowledge Base
Click Process Files to generate embeddings.

Generate Test Cases
Go to Test Case Agent and enter a prompt
Example:

Generate test cases for discount code


Generate Selenium Scripts
Select a test case → click Generate Selenium Script

📁 Project Structure
app/
 ├── backend/       # FastAPI + RAG logic
 ├── frontend/      # Streamlit UI
assets/             # HTML + documentation samples
data/               # Uploaded files + vector database

🧪 Example Test Case
Title: Apply valid discount code

Preconditions:
- User is on checkout page
- Cart contains at least one item

Steps:
1. Enter "SAVE20" in discount field
2. Click Apply

Expected Result:
- Total price reduces by 20%
- Success message displayed

🧪 Example Selenium Script (Simplified)
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///path/to/checkout.html")

driver.find_element(By.ID, "coupon").send_keys("SAVE20")
driver.find_element(By.ID, "apply-btn").click()

# Add assertions here

🤝 Contributing

Pull requests are welcome.
For major changes, please open an issue first
