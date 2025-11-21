import os
import json
import uuid
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from bs4 import BeautifulSoup

# Initialize Vector DB
# Persist in ./data/chroma_db
CHROMA_DB_DIR = os.path.join(os.getcwd(), "data", "chroma_db")
os.makedirs(CHROMA_DB_DIR, exist_ok=True)

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

# Use a local embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

class LocalEmbeddingFunction(chromadb.EmbeddingFunction):
    def __call__(self, input: chromadb.Documents) -> chromadb.Embeddings:
        return embedding_model.encode(input).tolist()

collection = client.get_or_create_collection(
    name="qa_agent_knowledge_base",
    embedding_function=LocalEmbeddingFunction()
)

def ingest_document(file_name: str, content: str, doc_type: str):
    """
    Ingests a document into the vector database.
    """
    chunks = []
    metadatas = []
    ids = []

    if doc_type == "html":
        soup = BeautifulSoup(content, 'html.parser')
        # Extract text but keep some structure if possible, or just raw text
        text = soup.get_text(separator="\n")
        # Split by lines or paragraphs
        raw_chunks = [t.strip() for t in text.split('\n') if t.strip()]
        # Group small chunks
        current_chunk = ""
        for rc in raw_chunks:
            if len(current_chunk) + len(rc) < 500:
                current_chunk += " " + rc
            else:
                chunks.append(current_chunk)
                current_chunk = rc
        if current_chunk:
            chunks.append(current_chunk)
            
    elif doc_type == "json":
        try:
            data = json.loads(content)
            # Flatten JSON to string
            text = json.dumps(data, indent=2)
            # Simple chunking
            chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
        except:
            chunks = [content]
            
    else: # md, txt
        # Simple recursive-like splitting (by paragraphs)
        raw_chunks = content.split('\n\n')
        chunks = [c.strip() for c in raw_chunks if c.strip()]

    for i, chunk in enumerate(chunks):
        chunks[i] = f"Source: {file_name}\nContent: {chunk}"
        metadatas.append({"source": file_name, "type": doc_type})
        ids.append(f"{file_name}_{i}_{str(uuid.uuid4())[:8]}")

    if chunks:
        collection.add(
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )
    return len(chunks)

def retrieve_context(query: str, n_results: int = 3) -> List[str]:
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results['documents'][0] if results['documents'] else []

def clear_knowledge_base():
    global collection
    client.delete_collection("qa_agent_knowledge_base")
    collection = client.get_or_create_collection(
        name="qa_agent_knowledge_base",
        embedding_function=LocalEmbeddingFunction()
    )

# --- LLM Integration ---

def call_llm(prompt: str, provider: str = "mock", api_key: str = None):
    """
    Calls an LLM. 
    Supported providers: 'mock', 'groq' (requires key).
    """
    if provider == "groq":
        if not api_key:
            return "Error: Groq API Key required."
        try:
            from groq import Groq
            client = Groq(api_key=api_key)
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error calling Groq: {str(e)}"
            
    else: # Mock
        # Return a dummy response based on the prompt content to look somewhat real
        if "test cases" in prompt.lower():
            return """
            [
                {
                    "Test_ID": "TC-001",
                    "Feature": "Discount Code",
                    "Test_Scenario": "Apply valid discount code SAVE15",
                    "Expected_Result": "15% discount applied to total",
                    "Grounded_In": "product_specs.md"
                },
                {
                    "Test_ID": "TC-002",
                    "Feature": "Shipping",
                    "Test_Scenario": "Select Express Shipping",
                    "Expected_Result": "$10 added to total",
                    "Grounded_In": "product_specs.md"
                }
            ]
            """
        elif "selenium" in prompt.lower():
            return """
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///path/to/checkout.html")

# Test Case: Apply valid discount code
code_input = driver.find_element(By.ID, "discount-code")
code_input.send_keys("SAVE15")
driver.find_element(By.XPATH, "//button[text()='Apply']").click()

time.sleep(1)
msg = driver.find_element(By.ID, "discount-msg").text
assert "15% Discount Applied" in msg

driver.quit()
```
            """
        return "Mock response: I received your request."
