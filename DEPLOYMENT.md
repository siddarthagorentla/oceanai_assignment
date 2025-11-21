# Deployment Guide

This project is designed to be deployed as two separate services: a **FastAPI Backend** and a **Streamlit Frontend**.

## Option 1: Docker Compose (Recommended for VPS/Local)
If you have a server with Docker installed (e.g., AWS EC2, DigitalOcean Droplet), this is the easiest method.

1. **Build and Run**:
   ```bash
   docker-compose up --build -d
   ```
2. **Access**:
   - Frontend: `http://<your-server-ip>:8501`
   - Backend: `http://<your-server-ip>:8000`

## Option 2: Render.com (Free Tier)
Render is a great platform for deploying this without managing servers. You will need to deploy two separate services.

### Step 1: Push Code to GitHub
Ensure your code is in a GitHub repository.

### Step 2: Deploy Backend (Web Service)
1. Create a new **Web Service** on Render.
2. Connect your GitHub repo.
3. **Settings**:
   - **Name**: `qa-agent-backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.backend.main:app --host 0.0.0.0 --port 10000`
4. Click **Create Web Service**.
5. Copy the URL (e.g., `https://qa-agent-backend.onrender.com`).

### Step 3: Deploy Frontend (Web Service)
1. Create another **Web Service** on Render.
2. Connect the same GitHub repo.
3. **Settings**:
   - **Name**: `qa-agent-frontend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app/frontend/ui.py --server.port $PORT --server.address 0.0.0.0`
4. **Environment Variables**:
   - Add a variable named `BACKEND_URL`.
   - Set the value to your Backend URL from Step 2 (e.g., `https://qa-agent-backend.onrender.com`).
5. Click **Create Web Service**.

### Step 4: Access
Visit your Frontend URL (e.g., `https://qa-agent-frontend.onrender.com`). It will automatically communicate with your deployed backend.

## Notes
- **Persistence**: On free tiers like Render, the local disk is ephemeral. This means if the server restarts, your uploaded files and Vector DB (Chroma) will be reset. For production, you would need to use a persistent disk or a cloud database.
- **API Keys**: If using Groq, remember to add `GROQ_API_KEY` as an environment variable in your deployment settings if you want to hardcode it, or just enter it in the UI as designed.
