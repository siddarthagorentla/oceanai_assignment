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
import re

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
            
    else: # A more intelligent mock
        # Extract context from the prompt
        context_match = re.search(r"Documentation Context:\s*([\s\S]*)User Request:", prompt)
        context = context_match.group(1).strip() if context_match else ""

        # Extract a relevant snippet from the context
        snippet = context.split('\n')[0][:100] # Take the first line or 100 chars as a snippet

        if "test cases" in prompt.lower():
            return f"""
            [
                {{
                    "Test_ID": "TC-MOCK-01",
                    "Feature": "Mock Feature",
                    "Test_Scenario": "Scenario based on context: '{snippet}...'",
                    "Expected_Result": "Expected result grounded in the context.",
                    "Grounded_In": "Provided Documentation"
                }}
            ]
            """
        elif "selenium" in prompt.lower():
            return f"""
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# This is a mock script and may require a real HTML file to run.
# It is based on the following context: {snippet}

driver = webdriver.Chrome()
# Make sure to provide the path to your actual HTML file
# driver.get("file:///path/to/your/checkout.html")

print("Mock script generated for context: {snippet}")
time.sleep(2)
print("Test completed.")

driver.quit()
```
            """
        return "Mock response: I received your request."
