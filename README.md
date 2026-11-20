# Cog Culture Placement Assessment: Management Trainee – Product

Comprehensive submission repository containing all deliverables for the **Cog Culture Placement Process** for the **Management Trainee – Product Profile**.

---

## 📌 Deliverables Overview

| Deliverable | Description | File / Asset Location |
|---|---|---|
| **1. Presentation Deck (Part 1)** | 10-slide executive PPTX deck covering the GEO (Generative Engine Optimization) product strategy, competitive landscape, feature blueprint, and monetization roadmap (3-month & 1-year).
| **2. Deployed Web Application (Part 2)** | Live "Fact-Check" Agent Web App that acts as a Truth Layer reading PDFs, cross-referencing claims against live web data, and flagging inaccuracies. | Ready to deploy on [Streamlit Cloud](https://share.streamlit.io) (see [Deployment Guide](#-deployment-to-streamlit-community-cloud-in-3-minutes)) |
| **3. GitHub Repository** | Clean, modular codebase with `app.py`, `fact_checker.py`, `requirements.txt`, sample trap documents, and comprehensive documentation. | Root Directory |
| **4. Demo Video** | 30-second screen recording walkthrough and recording storyboard for zero-credit evaluation. | [`demo_video_guide.md`](./demo_video_guide.md) |

---

## 🚀 Part 1: GEO Product Strategy Deck (`.pptx`)

The presentation [`CogCulture_GEO_Product_Strategy_Deck.pptx`](./CogCulture_GEO_Product_Strategy_Deck.pptx) is an executive-level deck formatted.


## 🛡️ Part 2: The "Fact-Check" Agent Web App (`FactShield AI`)

### The Objective & Architecture
Marketing collaterals and whitepapers often contain outdated metrics, hallucinated milestones, or exaggerated figures. **FactShield AI** acts as an enterprise Truth Layer:

```
┌─────────────────┐     ┌───────────────────────┐     ┌───────────────────────┐     ┌───────────────────────┐
│  Uploaded PDF   │ ──> │   Claim Extraction    │ ──> │    Live Web Search    │ ──> │   Truth Evaluation    │
│ (e.g. Trap Doc) │     │ (Stats, Dates, Money) │     │ (Wikipedia + Web API) │     │  & Scoring Engine     │
└─────────────────┘     └───────────────────────┘     └───────────────────────┘     └───────────────────────┘
                                                                                                │
                                                                                                ▼
                                                                                    ┌───────────────────────┐
                                                                                    │  Executive Scorecard  │
                                                                                    │  & Flagged Inaccuracy │
                                                                                    │   Report (CSV/JSON)   │
                                                                                    └───────────────────────┘
```

### 3-Tier Classification System:
- **Verified (Green)**: The claim matches authoritative factual and statistical records.
- **Inaccurate (Amber)**: The claim contains outdated statistics, wrong numerical magnitudes, wrong dates, or partial distortions.
- **False (Red)**: The claim is contradicted by known facts, a fabrication, hallucination, or an intentional lie.


---

## 💻 Local Quickstart

### 1. Set Up Environment
```bash
# Clone the repository
git clone <your-repo-url>
cd CogCulture

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Web Application
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### 3. Test Immediately
- Click the **"⚠️ Trap Doc"** button in the sidebar to run the pre-configured assessment trap test in one click.
- Or upload your own PDF whitepaper or marketing document.
- Optionally enter a Google Gemini or OpenAI API key in the sidebar for LLM mode.

---

## ☁️ Deployment Guides

### Option A: 1-Click Deployment to Render (Recommended)

This repository includes a pre-configured [`render.yaml`](./render.yaml) blueprint and [`Procfile`](./Procfile) for seamless deployment on [Render](https://render.com):

1. **Sign in to Render**:
   - Go to [dashboard.render.com](https://dashboard.render.com/) and sign in with your GitHub account.
2. **Deploy with Blueprint**:
   - Click **"New +"** in the top right ➔ Select **"Blueprint"**.
   - Connect your GitHub repository: `NikunjKhullar/cog-culture-factcheck`.
   - Render will automatically detect `render.yaml` with the configured Build and Start commands.
   - Click **"Apply"**.
3. **Manual Web Service (Alternative)**:
   - Click **"New +"** ➔ **"Web Service"** ➔ Select `cog-culture-factcheck`.
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0 --server.headless true --server.enableCORS false --server.enableXsrfProtection false`
   - **Plan**: Select **Free**.
   - Click **"Deploy Web Service"**.
4. **Live URL**:
   Your app will be live at:
   `https://cogculture-factshield.onrender.com`

---

### Option B: Deployment to Streamlit Community Cloud (in 2 Minutes)

The application is built specifically for **Streamlit Community Cloud**, fulfilling the mandatory deployment deliverable (`https://<your-app-name>.streamlit.app`):

1. **Push this project to a GitHub repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Cog Culture Assessment deliverables"
   git branch -M main
   git remote add origin https://github.com/<your-username>/cog-culture-factcheck.git
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
   - Click **"New App"**.
   - Select your repository (`cog-culture-factcheck`), Branch (`main`), and Main file path (`app.py`).
   - Click **"Deploy!"**.

3. **Your App URL**:
   Within 60 seconds, your application will be live at:
   `https://<your-custom-name>.streamlit.app`
   *(Copy this URL for Deliverable 2 in your submission email).*

---
