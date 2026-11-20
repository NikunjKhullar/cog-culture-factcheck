# Cog Culture Placement Assessment: Management Trainee – Product

Comprehensive submission repository containing all deliverables for the **Cog Culture Placement Process** for the **Management Trainee – Product Profile**.

---

## 📌 Deliverables Overview

| Deliverable | Description | File / Asset Location |
|---|---|---|
| **1. Presentation Deck (Part 1)** | 10-slide executive PPTX deck covering the GEO (Generative Engine Optimization) product strategy, competitive landscape, feature blueprint, and monetization roadmap (3-month & 1-year). | [`CogCulture_GEO_Product_Strategy_Deck.pptx`](./CogCulture_GEO_Product_Strategy_Deck.pptx) |
| **2. Deployed Web Application (Part 2)** | Live "Fact-Check" Agent Web App that acts as a Truth Layer reading PDFs, cross-referencing claims against live web data, and flagging inaccuracies. | Ready to deploy on [Streamlit Cloud](https://share.streamlit.io) (see [Deployment Guide](#-deployment-to-streamlit-community-cloud-in-3-minutes)) |
| **3. GitHub Repository** | Clean, modular codebase with `app.py`, `fact_checker.py`, `requirements.txt`, sample trap documents, and comprehensive documentation. | Root Directory |
| **4. Demo Video** | 30-second screen recording walkthrough and recording storyboard for zero-credit evaluation. | [`demo_video_guide.md`](./demo_video_guide.md) |

---

## 🚀 Part 1: GEO Product Strategy Deck (`.pptx`)

The generated presentation [`CogCulture_GEO_Product_Strategy_Deck.pptx`](./CogCulture_GEO_Product_Strategy_Deck.pptx) is an executive-level deck formatted in 16:9 widescreen:

### Executive Outline of Slides:
1. **Title Slide**: Generative Engine Optimization (GEO) – Product Strategy, Market Intelligence & Feature Blueprint.
2. **The Paradigm Shift**: Transition from Traditional SEO (Rankings, 10 blue links, click-throughs) to GEO (Conversational synthesis, zero-click answers, citation attribution, and Share of Model).
3. **Competitive Landscape**: Comprehensive comparison matrix benchmarking existing market tools:
   - **Profound** (Prompt tracking & mention frequency)
   - **AthenaHQ / Otterly.ai** (Perplexity & brand mentions)
   - **Peasy / Brandwatch** (AI search visibility)
   - **Cog Culture's GEO Platform** (Full multi-model tracking, live truth layer, citation graph, and automated knowledge schema injection).
4. **Detailed Feature Blueprint**: *"BrandShield AI: Real-Time Hallucination Sentinel & Citation Injection Engine"*
   - Multi-Prompt Simulation (100+ prompt mutations across ChatGPT, Gemini, Perplexity, Claude).
   - Citation Gap Analyzer (deconstructing synthesized answers into source URLs to identify where competitors dominate).
   - Truth Layer & Hallucination Sentinel (flags outdated specs before misinformation spreads).
   - Automated Knowledge Graph Schema Generator (prescribing JSON-LD schemas and markdown matrices).
5. **Short-Term Roadmap (Months 1 – 3)**:
   - Month 1: Multi-Model Benchmark Engine (direct API connectors for OpenAI, Google, Anthropic, Perplexity).
   - Month 2: Citation Attribution & Truth Layer MVP (brand dashboard with citation heatmaps).
   - Month 3: Remediation Engine & Commercial Launch (Slack alerts, self-serve onboarding, $15k MRR target).
6. **Long-Term Roadmap (Months 4 – 12)**:
   - Q2 (Months 4-6): Autonomous Content Optimizer & E-commerce Product Recommendation Tracker.
   - Q3 (Months 7-9): Multi-Lingual GEO across 12 languages & Multi-Modal visual search tracking.
   - Q4 (Months 10-12): Predictive GEO Trends & Enterprise Feed-to-LLM Syndication ($2.5M ARR run-rate).
7. **Monetization Strategy & Business Model**:
   - **Starter Plan**: $299/mo (50 prompts, 2 LLMs, weekly refresh).
   - **Growth Plan**: $899/mo (250 prompts, 5 LLMs, real-time alerts, schema playbook).
   - **Enterprise Plan**: $2,499+/mo (1,000+ custom prompts, full API, whitelabel agency portal).
   - Expansion revenue levers: Prompt pack add-ons, remediation credits, and agency rev-share.
8. **Technical Architecture**: Scalable asynchronous query queue, multi-model orchestrator, vector semantic drift caching, and webhook notification pipeline.
9. **Executive Metrics & Cog Culture Alignment**: North Star Metric (Brand Citation Share %), LTV/CAC > 4.5x, and why this platform positions Cog Culture as a pioneer in AI-native search.

*To re-generate or modify the deck at any time, run:*
```bash
python generate_deck.py
```

---

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

### 🧪 Evaluation Criteria & The "Trap Document"
The system was tested against [`sample_trap_document.pdf`](./sample_trap_document.pdf), designed to mirror evaluation trap tests:
1. **Outdated Stat**: Claims the 2024 global AI market was valued at "only $12 billion" ➔ **Flagged as Inaccurate** (Real 2024 market size: $184B – $214B).
2. **Intentional Lie**: Claims "Google Chrome was officially acquired by Microsoft for $50 billion" ➔ **Flagged as False** (Chrome is owned by Google; Microsoft develops Edge).
3. **Outdated Financial Milestone**: Claims Apple first reached a $1 trillion market cap in 2026 ➔ **Flagged as Inaccurate** (Apple reached $1T in 2018, and surpassed $3T in 2024).
4. **Economic Fabrication**: Claims enterprise software spending contracted by 45% in 2024 ➔ **Flagged as False** (Enterprise IT spending expanded by 8–12%).
5. **Gross Exaggeration**: Claims 1 ChatGPT query uses 500 liters of water ➔ **Flagged as Inaccurate** (Consumes ~500ml per 20–50 queries, a 10,000x exaggeration).
6. **Blatant Hallucination**: Claims Cog Culture was founded in 1845 as a steam locomotive maker ➔ **Flagged as False**.
7. **Control Verified Facts**: Correctly validates Perplexity AI's 2022 founding team and ChatGPT's 100M user milestone as **Verified**.

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

## ☁️ Deployment to Streamlit Community Cloud (in 3 Minutes)

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

## 📧 Final Submission Email Template

When submitting your assessment to Cog Culture, you can use the following format:

```text
Subject: Cog Culture Placement Process: Assessment Submission – Management Trainee (Product) – [Your Name]

Dear Devi Prasad & Cog Culture Team,

Thank you for the opportunity to participate in the placement process for the Management Trainee – Product profile. 

Please find attached my completed assessment deliverables:

1. Presentation Deck (Part 1):
   - Attached: CogCulture_GEO_Product_Strategy_Deck.pptx
   - Summary: Detailed feature blueprint ("BrandShield AI"), multi-tool competitive analysis (Profound, AthenaHQ, Peasy), and 3-month to 1-year product strategy & monetization roadmap for Generative Engine Optimization.

2. Deployed Application Link (Part 2):
   - Live URL: https://[your-app-name].streamlit.app

3. GitHub Repository:
   - Repository: https://github.com/[your-username]/[your-repo-name]
   - Contains clean code, requirements.txt, automated trap testing scripts, and comprehensive documentation.

4. Demo Video:
   - Video Link / File: [Google Drive link or attached 30-second screen recording]
   - Demonstrates the automated PDF fact-checking workflow against the trap document with live web verification.

I look forward to discussing my strategy and product execution during the evaluation interview.

Warm regards,
[Your Name]
[Your Phone Number]
[Your Email]
```
