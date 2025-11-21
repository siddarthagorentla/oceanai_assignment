import streamlit as st
import requests
import json
import os

# Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(
    page_title="Autonomous QA Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for "Premium" look
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #4CAF50; 
        color: white;
        border: none;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    h1 {
        color: #2c3e50;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 Autonomous QA Agent")
st.markdown("### AI-Powered Test Case & Script Generation")

# Sidebar for Configuration & Uploads
with st.sidebar:
    st.header("⚙️ Configuration")
    provider = st.selectbox("LLM Provider", ["mock", "groq"])
    api_key = ""
    if provider == "groq":
        api_key = st.text_input("Groq API Key", type="password")
    
    st.divider()
    
    st.header("📂 Knowledge Base")
    uploaded_files = st.file_uploader(
        "Upload Project Assets (HTML, MD, JSON)", 
        accept_multiple_files=True,
        type=['html', 'md', 'txt', 'json']
    )
    
    if st.button("Build Knowledge Base"):
        if uploaded_files:
            with st.spinner("Ingesting documents..."):
                files = [('files', (f.name, f, f.type)) for f in uploaded_files]
                try:
                    res = requests.post(f"{BACKEND_URL}/ingest", files=files)
                    if res.status_code == 200:
                        st.success("Knowledge Base Built Successfully!")
                    else:
                        st.error("Failed to build Knowledge Base.")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
        else:
            st.warning("Please upload files first.")

    if st.button("Reset Knowledge Base"):
        requests.post(f"{BACKEND_URL}/reset_kb")
        st.info("Knowledge Base Cleared.")

# Main Tabs
tab1, tab2 = st.tabs(["📝 Test Case Generation", "💻 Selenium Script Agent"])

with tab1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Generate Test Cases")
    
    user_query = st.text_area("Describe the feature to test:", "Generate positive and negative test cases for the discount code feature.")
    
    if st.button("Generate Test Cases"):
        with st.spinner("Analyzing Knowledge Base & Generating Cases..."):
            payload = {
                "query": user_query,
                "provider": provider,
                "api_key": api_key
            }
            try:
                res = requests.post(f"{BACKEND_URL}/generate_test_cases", json=payload)
                if res.status_code == 200:
                    data = res.json()
                    response_text = data.get("response", "")
                    st.session_state['last_test_cases'] = response_text
                    st.markdown(response_text)
                else:
                    st.error(f"Error: {res.text}")
            except Exception as e:
                st.error(f"Connection Error: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.subheader("Generate Selenium Scripts")
    
    # Input for test case (can be pasted or selected from previous)
    default_tc = st.session_state.get('last_test_cases', "")
    test_case_input = st.text_area("Paste a Test Case here:", default_tc, height=200)
    
    if st.button("Generate Selenium Script"):
        if not test_case_input:
            st.warning("Please provide a test case.")
        else:
            with st.spinner("Generating Selenium Script..."):
                payload = {
                    "test_case_str": test_case_input,
                    "provider": provider,
                    "api_key": api_key
                }
                try:
                    res = requests.post(f"{BACKEND_URL}/generate_script", json=payload)
                    if res.status_code == 200:
                        script = res.json().get("script", "")
                        st.code(script, language='python')
                    else:
                        st.error(f"Error: {res.text}")
                except Exception as e:
                    st.error(f"Connection Error: {e}")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Developed for OceanAI Assignment")
