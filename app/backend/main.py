from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
import shutil
import os
from pydantic import BaseModel

from app.backend.rag_service import ingest_document, retrieve_context, call_llm, clear_knowledge_base
from app.backend.models import TestCaseResponse, ScriptResponse

app = FastAPI(title="Autonomous QA Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = os.path.join(os.getcwd(), "data", "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)

class GenerateRequest(BaseModel):
    query: str
    provider: str = "mock"
    api_key: Optional[str] = None

class ScriptGenRequest(BaseModel):
    test_case_str: str
    provider: str = "mock"
    api_key: Optional[str] = None

@app.post("/ingest")
async def ingest_files(files: List[UploadFile] = File(...)):
    count = 0
    for file in files:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Read content
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        ext = file.filename.split('.')[-1].lower()
        doc_type = "html" if ext == "html" else "json" if ext == "json" else "text"
        
        ingest_document(file.filename, content, doc_type)
        count += 1
    
    return {"message": f"Successfully ingested {count} files."}

@app.post("/reset_kb")
async def reset_kb():
    clear_knowledge_base()
    return {"message": "Knowledge base cleared."}

@app.post("/generate_test_cases")
async def generate_test_cases(req: GenerateRequest):
    context = retrieve_context(req.query, n_results=5)
    context_str = "\n\n".join(context)
    
    prompt = f"""
    You are an expert QA Engineer. Based on the following project documentation, generate comprehensive test cases for the user's request.
    
    Documentation Context:
    {context_str}
    
    User Request: {req.query}
    
    Output Format:
    Provide a JSON list of test cases. Each test case must have:
    - Test_ID
    - Feature
    - Test_Scenario
    - Expected_Result
    - Grounded_In (The specific document name)
    
    Do not hallucinate features. Only use what is in the context.
    """
    
    response = call_llm(prompt, req.provider, req.api_key)
    return {"response": response}

@app.post("/generate_script")
async def generate_script(req: ScriptGenRequest):
    # Retrieve context specifically for script generation (HTML structure is key)
    # We assume the HTML was ingested and will be retrieved if we query for "HTML" or "selectors"
    context = retrieve_context("checkout.html structure selectors ids", n_results=3)
    context_str = "\n\n".join(context)
    
    prompt = f"""
    You are an expert Selenium Python Automation Engineer.
    Generate a robust, runnable Selenium script for the following test case.
    
    Test Case:
    {req.test_case_str}
    
    Context (HTML & Rules):
    {context_str}
    
    Requirements:
    - Use 'webdriver.Chrome()'
    - Use explicit waits (WebDriverWait) where appropriate.
    - Use correct selectors (ID, CSS, XPath) based on the context provided.
    - Include assertions.
    - Return ONLY the code block.
    """
    
    response = call_llm(prompt, req.provider, req.api_key)
    return {"script": response}
