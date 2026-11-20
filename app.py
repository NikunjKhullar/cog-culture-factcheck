"""
FactShield AI - Automated Truth Layer & Fact-Checking Agent
Assessment Submission for Cog Culture Placement Process (Management Trainee - Product)
"""

import os
import json
import pandas as pd
import streamlit as st
from io import BytesIO
import fact_checker

# Configure Streamlit Page
st.set_page_config(
    page_title="FactShield AI | Truth Layer Fact-Checker",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Modern UI
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background-color: #F8FAFC;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Top Banner */
    .hero-container {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        padding: 2.2rem 2.5rem;
        border-radius: 14px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.2);
        border: 1px solid #334155;
    }
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        color: #FFFFFF;
        letter-spacing: -0.5px;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #94A3B8;
        margin-top: 0.6rem;
        line-height: 1.5;
    }
    .hero-pill {
        display: inline-block;
        background: rgba(14, 165, 233, 0.15);
        color: #38BDF8;
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Scorecard Metrics */
    .metric-card {
        background: white;
        padding: 1.4rem;
        border-radius: 12px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
    }
    .metric-val {
        font-size: 2.4rem;
        font-weight: 800;
        line-height: 1.1;
    }
    .metric-label {
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        color: #64748B;
        margin-top: 0.4rem;
    }

    /* Claim Cards */
    .claim-card {
        background: white;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
    }
    .badge-verified {
        background-color: #DCFCE7;
        color: #15803D;
        border: 1px solid #86EFAC;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.82rem;
        display: inline-block;
    }
    .badge-inaccurate {
        background-color: #FEF3C7;
        color: #B45309;
        border: 1px solid #FCD34D;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.82rem;
        display: inline-block;
    }
    .badge-false {
        background-color: #FEE2E2;
        color: #B91C1C;
        border: 1px solid #FCA5A5;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: 700;
        font-size: 0.82rem;
        display: inline-block;
    }
    .reality-box {
        background-color: #F8FAFC;
        border-left: 4px solid #0EA5E9;
        padding: 0.9rem 1.1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.9rem 0;
    }
    .reality-title {
        font-weight: 700;
        color: #0369A1;
        font-size: 0.88rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.2rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=300&auto=format&fit=crop&q=60", width=260)
    st.markdown("### 🏢 Cog Culture Placement")
    st.caption("**Profile:** Management Trainee – Product")
    st.caption("**Assessment:** Part 2 - The 'Fact-Check' Agent")
    st.divider()

    st.markdown("#### ⚙️ Engine Settings")
    engine_mode = st.radio(
        "Verification Engine Mode",
        options=["Free Live Web & Knowledge Graph (Default)", "LLM + Live Web (Gemini / OpenAI)"],
        index=0,
        help="The Free engine runs 100% out-of-the-box without requiring API keys or incurring costs."
    )

    api_key = ""
    provider = "gemini"
    if "LLM" in engine_mode:
        provider = st.selectbox("LLM Provider", ["gemini", "openai"], index=0)
        api_key = st.text_input(
            f"{provider.capitalize()} API Key",
            type="password",
            help="Enter your API key. If left blank, the app will seamlessly use the built-in search engine."
        )

    st.divider()
    st.markdown("#### 🧪 One-Click Test Documents")
    st.info("Evaluate instantly using the pre-configured assessment documents:")
    
    col_t1, col_t2 = st.columns(2)
    load_trap = col_t1.button("⚠️ Trap Doc", use_container_width=True, help="Document with intentional lies & outdated stats")
    load_valid = col_t2.button("✅ Valid Doc", use_container_width=True, help="Document with accurate facts")

    st.divider()
    st.caption("🛡️ **FactShield AI v1.0** • Built for automated marketing truth verification.")

# Top Hero Header
st.markdown("""
<div class="hero-container">
    <div class="hero-pill">Truth Layer for Marketing Intelligence</div>
    <h1 class="hero-title">FactShield AI: Automated PDF Claim Verification</h1>
    <div class="hero-subtitle">
        Marketing collateral and whitepapers frequently cite outdated statistics, hallucinated milestones, or fabricated claims. 
        This agent reads uploaded PDFs, extracts discrete factual claims, searches the live web in real time, and flags inaccuracies with verified ground truth.
    </div>
</div>
""", unsafe_allow_html=True)

# Handle Session State for Document Testing
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "active_doc_name" not in st.session_state:
    st.session_state.active_doc_name = None

# Quick-load triggers
target_pdf = None
doc_label = ""

if load_trap:
    if os.path.exists("sample_trap_document.pdf"):
        with open("sample_trap_document.pdf", "rb") as f:
            target_pdf = f.read()
            doc_label = "sample_trap_document.pdf (Official Trap Assessment Document)"
            st.session_state.active_doc_name = doc_label
            st.session_state.analysis_result = None

if load_valid:
    if os.path.exists("sample_valid_document.pdf"):
        with open("sample_valid_document.pdf", "rb") as f:
            target_pdf = f.read()
            doc_label = "sample_valid_document.pdf (Accurate Control Benchmark)"
            st.session_state.active_doc_name = doc_label
            st.session_state.analysis_result = None

# Upload Section
col_up1, col_up2 = st.columns([3, 1])

with col_up1:
    uploaded_file = st.file_uploader(
        "Upload a PDF Document to Fact-Check",
        type=["pdf"],
        help="Upload whitepapers, press releases, reports, or pitch decks."
    )

with col_up2:
    st.markdown("<div style='height: 28px'></div>", unsafe_allow_html=True)
    run_btn = st.button("🔍 Run Fact-Check", type="primary", use_container_width=True)

# Select which file to analyze
file_to_process = None
if uploaded_file is not None:
    file_to_process = uploaded_file
    doc_label = uploaded_file.name
elif target_pdf is not None:
    file_to_process = target_pdf

# Trigger Fact-Checking
if (run_btn or target_pdf is not None) and file_to_process is not None:
    progress_bar = st.progress(0)
    status_box = st.empty()

    def update_prog(val, msg):
        progress_bar.progress(val)
        status_box.info(f"⏳ **{msg}**")

    try:
        with st.spinner("Analyzing document..."):
            result = fact_checker.run_full_fact_check(
                file_to_process,
                api_key=api_key,
                provider=provider,
                progress_callback=update_prog
            )
            st.session_state.analysis_result = result
            st.session_state.active_doc_name = doc_label
            progress_bar.empty()
            status_box.empty()
            st.success(f"✅ Fact-checking completed for **{doc_label}**!")
    except Exception as e:
        progress_bar.empty()
        status_box.empty()
        st.error(f"❌ Fact-check failed: {str(e)}")

# Display Results
res = st.session_state.analysis_result
if res is not None:
    st.markdown("---")
    st.subheader(f"📊 Fact-Check Scorecard: {st.session_state.active_doc_name}")

    # Metrics Row
    m1, m2, m3, m4, m5 = st.columns(5)
    
    score_color = "#10B981" if res["truth_score"] >= 75 else ("#F59E0B" if res["truth_score"] >= 50 else "#EF4444")
    
    with m1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val" style="color: {score_color}">{res['truth_score']}%</div>
            <div class="metric-label">Truth Score</div>
        </div>
        """, unsafe_allow_html=True)
        
    with m2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val" style="color: #0F172A">{res['total_claims']}</div>
            <div class="metric-label">Claims Extracted</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val" style="color: #10B981">{res['counts'].get('Verified', 0)}</div>
            <div class="metric-label">Verified (Valid)</div>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val" style="color: #F59E0B">{res['counts'].get('Inaccurate', 0)}</div>
            <div class="metric-label">Inaccurate (Outdated)</div>
        </div>
        """, unsafe_allow_html=True)

    with m5:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-val" style="color: #EF4444">{res['counts'].get('False', 0)}</div>
            <div class="metric-label">False (Fabricated)</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 1.5rem'></div>", unsafe_allow_html=True)

    # Tabs for claim exploration
    tab_all, tab_flagged, tab_verified, tab_text = st.tabs([
        f"📋 All Claims ({res['total_claims']})",
        f"🚨 Flagged Inaccuracies ({res['counts'].get('Inaccurate', 0) + res['counts'].get('False', 0)})",
        f"✅ Verified Claims ({res['counts'].get('Verified', 0)})",
        "📄 Raw Document Text"
    ])

    def render_claim_card(c):
        verdict = c["verdict"]
        badge_class = "badge-verified" if verdict == "Verified" else ("badge-inaccurate" if verdict == "Inaccurate" else "badge-false")
        badge_symbol = "✓" if verdict == "Verified" else ("⚠" if verdict == "Inaccurate" else "✖")
        
        st.markdown(f"""
        <div class="claim-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                <span class="{badge_class}">{badge_symbol} {verdict.upper()} ({int(c['confidence']*100)}% Confidence)</span>
                <span style="font-size: 0.8rem; color: #94A3B8; font-weight: 600;">Claim #{c['id']} • {c.get('category', 'Stat').title()}</span>
            </div>
            <div style="font-size: 1.05rem; font-weight: 600; color: #1E293B; line-height: 1.4; margin-bottom: 0.6rem;">
                "{c['claim_text']}"
            </div>
            <div class="reality-box">
                <div class="reality-title">🔍 Verified Ground Truth / Reality:</div>
                <div style="color: #0F172A; font-size: 0.95rem; line-height: 1.4;">{c['real_fact']}</div>
            </div>
            <div style="font-size: 0.88rem; color: #475569; margin-top: 0.5rem;">
                <b>Agent Reasoning:</b> {c['explanation']}
            </div>
        """, unsafe_allow_html=True)

        if c.get("sources"):
            st.markdown("<div style='font-size: 0.82rem; color: #64748B; margin-top: 0.5rem;'><b>Live Sources Cited:</b></div>", unsafe_allow_html=True)
            cols = st.columns(len(c["sources"][:3]))
            for idx, s in enumerate(c["sources"][:3]):
                with cols[idx]:
                    st.markdown(f"🔗 [{s.split('//')[-1].split('/')[0]}]({s})")

        st.markdown("</div>", unsafe_allow_html=True)

    with tab_all:
        for c in res["claims"]:
            render_claim_card(c)

    with tab_flagged:
        flagged = [c for c in res["claims"] if c["verdict"] in ["Inaccurate", "False"]]
        if flagged:
            for c in flagged:
                render_claim_card(c)
        else:
            st.success("🎉 No inaccuracies detected! All extracted claims were verified against live records.")

    with tab_verified:
        verified = [c for c in res["claims"] if c["verdict"] == "Verified"]
        if verified:
            for c in verified:
                render_claim_card(c)
        else:
            st.warning("No verified claims found.")

    with tab_text:
        st.text_area("Extracted Document Text", res["raw_text"], height=320)

    # Export Report Options
    st.divider()
    st.subheader("📥 Export Fact-Check Report")
    
    col_dl1, col_dl2 = st.columns(2)
    
    # JSON Export
    json_data = json.dumps(res, indent=2)
    col_dl1.download_button(
        label="Download Full JSON Report",
        data=json_data,
        file_name="fact_check_report.json",
        mime="application/json",
        use_container_width=True
    )

    # CSV Export
    csv_rows = []
    for c in res["claims"]:
        csv_rows.append({
            "Claim ID": c["id"],
            "Original Claim": c["claim_text"],
            "Verdict": c["verdict"],
            "Confidence": c["confidence"],
            "Ground Truth": c["real_fact"],
            "Agent Explanation": c["explanation"],
            "Sources": "; ".join(c.get("sources", []))
        })
    df = pd.DataFrame(csv_rows)
    csv_data = df.to_csv(index=False).encode('utf-8')
    col_dl2.download_button(
        label="Download Clean CSV Report",
        data=csv_data,
        file_name="fact_check_report.csv",
        mime="text/csv",
        use_container_width=True
    )
else:
    # Empty State Guidance
    st.info("👆 Upload any PDF or click **'⚠️ Trap Doc'** in the sidebar to test with the official evaluation document containing intentional lies and outdated statistics.")
