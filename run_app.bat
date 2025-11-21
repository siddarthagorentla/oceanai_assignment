@echo off
echo Starting Autonomous QA Agent...

echo Installing dependencies...
pip install -r requirements.txt

echo Starting Backend...
start cmd /k "uvicorn app.backend.main:app --reload --port 8000"

echo Waiting for Backend to initialize...
timeout /t 5

echo Starting Frontend...
start cmd /k "streamlit run app/frontend/ui.py"

echo Done! Access the UI at http://localhost:8501
pause
