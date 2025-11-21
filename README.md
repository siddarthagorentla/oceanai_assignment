# Autonomous QA Agent for Test Case and Script Generation

## Overview
This project is an intelligent, autonomous QA agent that constructs a "testing brain" from project documentation and HTML structure. It generates comprehensive test cases and executable Selenium Python scripts grounded in the provided documentation.

## Features
- **Knowledge Base Ingestion**: Upload support documents (MD, TXT, JSON) and HTML to build a vector database.
- **Test Case Generation**: Generate positive and negative test cases based on the ingested knowledge.
- **Selenium Script Generation**: Convert selected test cases into runnable Selenium scripts.
- **RAG Pipeline**: Uses Retrieval-Augmented Generation to ensure all outputs are grounded in the provided documents.

## Setup Instructions

### Prerequisites
- Python 3.9+
- Chrome Browser (for Selenium execution)

### Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application
The application consists of a FastAPI backend and a Streamlit frontend.

1. **Start the Backend**:
   Open a terminal and run:
   ```bash
   uvicorn app.backend.main:app --reload --port 8000
   ```

2. **Start the Frontend**:
   Open a new terminal and run:
   ```bash
   streamlit run app/frontend/ui.py
   ```

3. **Access the UI**:
   Open your browser and go to `http://localhost:8501`.

### Workflow
1. **Upload Assets**: Go to the sidebar/upload section. Upload `checkout.html` and the support documents from the `assets/` folder.
2. **Build Knowledge Base**: Click the button to process files and create embeddings.
3. **Generate Test Cases**: Go to the "Test Case Agent" tab. Enter a prompt (e.g., "Generate test cases for discount code").
4. **Generate Scripts**: Select a generated test case and click "Generate Selenium Script".

## Project Structure
- `app/backend`: FastAPI application and RAG logic.
- `app/frontend`: Streamlit user interface.
- `assets`: Sample project files (`checkout.html`, specs, etc.).
- `data`: Storage for uploaded files and vector database.
