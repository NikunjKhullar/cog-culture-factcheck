"""
FactShield AI - 3D Dynamic Truth Layer & Fact-Checking Web Application
Design inspired by Canva & Google Stitch Design System.
Powered by Sarvam AI Document OCR & Gamma 4 (31B) Reasoning Engine.
"""

import os
import json
import pandas as pd
import streamlit as st
from io import BytesIO
import importlib
import fact_checker
importlib.reload(fact_checker)

# Configure Streamlit Page
st.set_page_config(
    page_title="FactShield AI | 3D Truth Layer & Gamma 4 Agent",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Canva & Google Stitch Inspired 3D Animated Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

    :root {
        --stitch-bg: #0B0F19;
        --stitch-card: rgba(18, 24, 38, 0.75);
        --stitch-card-border: rgba(255, 255, 255, 0.08);
        --canva-purple: #7C3AED;
        --canva-cyan: #06B6D4;
        --canva-blue: #3B82F6;
        --emerald-glow: #10B981;
        --amber-glow: #F59E0B;
        --rose-glow: #F43F5E;
    }

    /* Dynamic Mesh Background */
    .stApp {
        background-color: var(--stitch-bg);
        background-image: 
            radial-gradient(at 0% 0%, rgba(124, 58, 237, 0.15) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(6, 182, 212, 0.15) 0px, transparent 50%),
            radial-gradient(at 50% 100%, rgba(59, 130, 246, 0.1) 0px, transparent 50%);
        font-family: 'Plus Jakarta Sans', sans-serif;
        color: #F8FAFC;
    }

    /* 3D Animated Hero Header */
    .hero-box {
        position: relative;
        background: linear-gradient(135deg, rgba(25, 33, 52, 0.85) 0%, rgba(15, 20, 32, 0.95) 100%);
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 20px;
        padding: 2.5rem;
        margin-bottom: 2rem;
        transform: perspective(1000px) rotateX(1deg);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        overflow: hidden;
    }
    .hero-box:hover {
        transform: perspective(1000px) rotateX(0deg) translateY(-2px);
        box-shadow: 0 25px 60px rgba(124, 58, 237, 0.18);
    }
    
    .hero-glow-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: linear-gradient(90deg, rgba(124, 58, 237, 0.25), rgba(6, 182, 212, 0.25));
        border: 1px solid rgba(6, 182, 212, 0.4);
        color: #67E8F9;
        padding: 6px 14px;
        border-radius: 30px;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        margin-bottom: 1rem;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.2);
    }

    .hero-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.5rem;
        font-weight: 700;
        background: linear-gradient(135deg, #FFFFFF 30%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1.2;
    }

    .hero-subtitle {
        color: #94A3B8;
        font-size: 1.05rem;
        margin-top: 0.8rem;
        line-height: 1.6;
        max-width: 900px;
    }

    /* Policy Shield Banner */
    .policy-banner {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 1.2rem;
        padding-top: 1.2rem;
        border-top: 1px solid rgba(255, 255, 255, 0.08);
    }
    .policy-chip {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.78rem;
        padding: 4px 10px;
        border-radius: 8px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #CBD5E1;
    }
    .policy-chip.blocked {
        border-color: rgba(244, 63, 94, 0.3);
        background: rgba(244, 63, 94, 0.08);
        color: #FDA4AF;
    }
    .policy-chip.allowed {
        border-color: rgba(16, 185, 129, 0.3);
        background: rgba(16, 185, 129, 0.08);
        color: #6EE7B7;
    }

    /* 3D Animated Metric Cards */
    .metric-card-3d {
        background: linear-gradient(145deg, rgba(26, 34, 54, 0.7) 0%, rgba(15, 21, 35, 0.9) 100%);
        border: 1px solid var(--stitch-card-border);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(12px);
        transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .metric-card-3d:hover {
        transform: translateY(-4px) scale(1.02);
        border-color: rgba(124, 58, 237, 0.4);
        box-shadow: 0 15px 35px rgba(124, 58, 237, 0.2);
    }
    .metric-num {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        line-height: 1;
        margin-bottom: 0.4rem;
    }
    .metric-label {
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94A3B8;
    }

    /* 3D Claim Cards */
    .claim-card-3d {
        background: linear-gradient(145deg, rgba(22, 28, 45, 0.8) 0%, rgba(13, 18, 30, 0.95) 100%);
        border: 1px solid rgba(255, 255, 255, 0.07);
        border-radius: 16px;
        padding: 1.6rem;
        margin-bottom: 1.3rem;
        box-shadow: 0 12px 28px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(16px);
        transition: all 0.3s ease;
    }
    .claim-card-3d:hover {
        border-color: rgba(255, 255, 255, 0.18);
        box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
    }

    /* Hologram Badges */
    .holo-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 0.6px;
    }
    .holo-verified {
        background: rgba(16, 185, 129, 0.15);
        border: 1px solid #10B981;
        color: #34D399;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.25);
    }
    .holo-inaccurate {
        background: rgba(245, 158, 11, 0.15);
        border: 1px solid #F59E0B;
        color: #FBBF24;
        box-shadow: 0 0 12px rgba(245, 158, 11, 0.25);
    }
    .holo-false {
        background: rgba(244, 63, 94, 0.15);
        border: 1px solid #F43F5E;
        color: #FB7185;
        box-shadow: 0 0 12px rgba(244, 63, 94, 0.25);
    }

    /* Reality Box (Google Stitch Accent) */
    .reality-box-stitch {
        background: linear-gradient(135deg, rgba(6, 182, 212, 0.08) 0%, rgba(59, 130, 246, 0.04) 100%);
        border-left: 4px solid #06B6D4;
        border-radius: 0 12px 12px 0;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
    }
    .reality-label {
        color: #38BDF8;
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-bottom: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="font-family: 'Space Grotesk', sans-serif; font-size: 1.6rem; font-weight: 700; background: linear-gradient(135deg, #7C3AED, #06B6D4); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            FactShield AI
        </div>
        <div style="font-size: 0.8rem; color: #94A3B8; margin-top: 4px;">Cog Culture Placement Process</div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    st.markdown("#### 🧠 Document Verification Engine")
    use_sarvam = st.toggle("Enable Sarvam AI (OCR & Extraction)", value=False, help="Connects to Sarvam AI Document Intelligence API (api.sarvam.ai) for multilingual & enterprise OCR.")
    sarvam_key = ""
    if use_sarvam:
        sarvam_key = st.text_input("Sarvam API Subscription Key", type="password", help="Enter api-subscription-key from api.sarvam.ai")

    st.markdown("#### ⚡ Reasoning Model")
    reasoning_model = st.selectbox(
        "Verification LLM",
        ["Gamma 4 (31B Grounded Hybrid)", "Gemma 31B via Open API", "Standard High-Precision Truth Layer"],
        index=0
    )
    gemma_key = ""
    if "Gemma" in reasoning_model or "Gamma" in reasoning_model:
        gemma_key = st.text_input("Gamma / Gemma API Key (Optional)", type="password", help="Leave blank to use the built-in live government & research ground-truth engine.")

    st.divider()
    st.markdown("#### 🛡️ Enforced Policy")
    st.caption("✅ **Strictly Included:** Government data (`.gov`, `.gov.in`, `sec.gov`, `census.gov`) and Peer-Reviewed Papers (`arXiv`, `PubMed/NIH`, `Nature`, `Science`).")
    st.caption("🚫 **Strictly Excluded:** Social media (`Twitter/X`, `Reddit`, `Facebook`, `Quora`, `Instagram`) and unverified third parties.")

    st.divider()
    st.markdown("#### 🧪 One-Click Trap Evaluation")
    st.caption("Test the assignment trap document with intentional lies and outdated statistics:")
    col_t1, col_t2 = st.columns(2)
    load_trap = col_t1.button("⚠️ Trap Doc", use_container_width=True)
    load_valid = col_t2.button("✅ Control Doc", use_container_width=True)

    st.divider()
    st.caption("💾 **Local Archive Active:** Uploaded PDFs are stored in `./uploads/` and generated audit reports in `./reports/`.")

# Hero Header
st.markdown("""
<div class="hero-box">
    <div class="hero-glow-badge">
        <span>✨ Powered by Sarvam AI & Gamma 4 (31B)</span>
    </div>
    <div class="hero-title">FactShield AI: Dynamic Truth Layer Agent</div>
    <div class="hero-subtitle">
        Automated document claim verification. Reads uploaded marketing PDFs, extracts discrete numerical, financial, 
        and technical claims, cross-references against live Government websites and peer-reviewed research papers, 
        and flags inaccuracies with verified ground truth facts.
    </div>
    <div class="policy-banner">
        <span class="policy-chip allowed">🏛️ Government Registries (.gov, .gov.in, SEC EDGAR)</span>
        <span class="policy-chip allowed">🔬 Academic Research (arXiv, PubMed/NIH, Nature, Science)</span>
        <span class="policy-chip blocked">🚫 Social Media Filtered Out (Twitter/X, Reddit, Quora, FB)</span>
        <span class="policy-chip allowed">💾 Automatic Local Archiving Active</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Session State
if "analysis_result" not in st.session_state:
    st.session_state.analysis_result = None
if "active_doc_name" not in st.session_state:
    st.session_state.active_doc_name = None

target_pdf = None
doc_label = ""

if load_trap:
    if os.path.exists("sample_trap_document.pdf"):
        with open("sample_trap_document.pdf", "rb") as f:
            target_pdf = f.read()
            doc_label = "sample_trap_document.pdf (Official Assessment Trap Document)"
            st.session_state.active_doc_name = doc_label
            st.session_state.analysis_result = None

if load_valid:
    if os.path.exists("sample_valid_document.pdf"):
        with open("sample_valid_document.pdf", "rb") as f:
            target_pdf = f.read()
            doc_label = "sample_valid_document.pdf (Accurate Benchmark Control Document)"
            st.session_state.active_doc_name = doc_label
            st.session_state.analysis_result = None

# Upload Section
col_u1, col_u2 = st.columns([3, 1])
with col_u1:
    uploaded_file = st.file_uploader(
        "Upload PDF Document for Automated Fact-Checking",
        type=["pdf"],
        help="Upload whitepapers, reports, pitch decks, or assessment trap documents."
    )

with col_u2:
    st.markdown("<div style='height: 28px'></div>", unsafe_allow_html=True)
    run_btn = st.button("🚀 Verify with Gamma 4", type="primary", use_container_width=True)

file_to_process = None
if uploaded_file is not None:
    file_to_process = uploaded_file
    doc_label = uploaded_file.name
elif target_pdf is not None:
    file_to_process = target_pdf

# Trigger Analysis
if (run_btn or target_pdf is not None) and file_to_process is not None:
    prog_bar = st.progress(0)
    status_msg = st.empty()

    def update_callback(p, msg):
        prog_bar.progress(p)
        status_msg.info(f"⚡ **{msg}**")

    try:
        with st.spinner("Analyzing document..."):
            res = fact_checker.run_full_fact_check(
                file_to_process,
                sarvam_api_key=sarvam_key,
                gemma_api_key=gemma_key,
                original_filename=doc_label,
                progress_callback=update_callback
            )
            st.session_state.analysis_result = res
            st.session_state.active_doc_name = doc_label
            prog_bar.empty()
            status_msg.empty()
            st.success(f"✅ Document verified successfully! Saved to `./uploads/` and report to `./reports/`.")
    except Exception as e:
        prog_bar.empty()
        status_msg.empty()
        st.error(f"❌ Error during verification: {str(e)}")

# Display Results
res = st.session_state.analysis_result
if res is not None:
    st.markdown("---")
    st.subheader(f"📊 Fact-Check Scorecard: {st.session_state.active_doc_name}")

    # Metrics Row
    m1, m2, m3, m4, m5 = st.columns(5)
    score_color = "#10B981" if res["truth_score"] >= 75 else ("#F59E0B" if res["truth_score"] >= 50 else "#F43F5E")

    with m1:
        st.markdown(f"""
        <div class="metric-card-3d">
            <div class="metric-num" style="color: {score_color};">{res['truth_score']}%</div>
            <div class="metric-label">Document Truth Score</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric-card-3d">
            <div class="metric-num" style="color: #F8FAFC;">{res['total_claims']}</div>
            <div class="metric-label">Claims Extracted</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-card-3d">
            <div class="metric-num" style="color: #34D399;">{res['counts'].get('Verified', 0)}</div>
            <div class="metric-label">Verified (Valid)</div>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown(f"""
        <div class="metric-card-3d">
            <div class="metric-num" style="color: #FBBF24;">{res['counts'].get('Inaccurate', 0)}</div>
            <div class="metric-label">Inaccurate (Outdated)</div>
        </div>
        """, unsafe_allow_html=True)

    with m5:
        st.markdown(f"""
        <div class="metric-card-3d">
            <div class="metric-num" style="color: #FB7185;">{res['counts'].get('False', 0)}</div>
            <div class="metric-label">False (Fabricated)</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 1.5rem'></div>", unsafe_allow_html=True)

    # Tabs
    tab_all, tab_flagged, tab_verified, tab_storage, tab_raw = st.tabs([
        f"📋 All Claims ({res['total_claims']})",
        f"🚨 Flagged Inaccuracies ({res['counts'].get('Inaccurate', 0) + res['counts'].get('False', 0)})",
        f"✅ Verified Claims ({res['counts'].get('Verified', 0)})",
        "💾 Local Storage Archive",
        "📄 Extracted Document Text"
    ])

    def render_claim_card(c):
        v = c["verdict"]
        badge_style = "holo-verified" if v == "Verified" else ("holo-inaccurate" if v == "Inaccurate" else "holo-false")
        icon = "✓" if v == "Verified" else ("⚠" if v == "Inaccurate" else "✖")
        
        st.markdown(f"""
        <div class="claim-card-3d">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.8rem;">
                <span class="holo-badge {badge_style}">{icon} {v.upper()} ({int(c['confidence']*100)}% Confidence)</span>
                <span style="font-size: 0.8rem; color: #64748B; font-weight: 600;">Claim #{c['id']} • {c.get('category', 'Stat').title()}</span>
            </div>
            <div style="font-size: 1.1rem; font-weight: 600; color: #F1F5F9; line-height: 1.5; margin-bottom: 0.8rem;">
                "{c['claim_text']}"
            </div>
            <div class="reality-box-stitch">
                <div class="reality-label">🔍 Authoritative Ground Truth / Reality:</div>
                <div style="color: #E2E8F0; font-size: 0.95rem; line-height: 1.5;">{c['real_fact']}</div>
            </div>
            <div style="font-size: 0.88rem; color: #94A3B8; margin-top: 0.5rem;">
                <b style="color: #CBD5E1;">Gamma 4 Agent Analysis:</b> {c['explanation']}
            </div>
        """, unsafe_allow_html=True)

        if c.get("sources"):
            st.markdown("<div style='font-size: 0.82rem; color: #64748B; margin-top: 0.6rem;'><b style='color: #94A3B8;'>Verified Against Government & Research Sources:</b></div>", unsafe_allow_html=True)
            cols = st.columns(len(c["sources"][:3]))
            for idx, s in enumerate(c["sources"][:3]):
                with cols[idx]:
                    domain = s.split('//')[-1].split('/')[0]
                    st.markdown(f"🔗 [`{domain}`]({s})")

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
            st.success("🎉 No inaccuracies detected! All claims verified against authoritative records.")

    with tab_verified:
        verified = [c for c in res["claims"] if c["verdict"] == "Verified"]
        if verified:
            for c in verified:
                render_claim_card(c)
        else:
            st.warning("No verified claims found.")

    with tab_storage:
        st.markdown("### 💾 Local File System Verification")
        st.info("The application automatically persists all uploaded documents and generated audit reports to your local machine:")
        st.write(f"📁 **Saved PDF Path:** `{res.get('saved_pdf_path', 'N/A')}`")
        if "saved_report_paths" in res:
            st.write(f"📄 **Saved JSON Audit Report:** `{res['saved_report_paths'].get('json', 'N/A')}`")
            st.write(f"📊 **Saved CSV Audit Report:** `{res['saved_report_paths'].get('csv', 'N/A')}`")

    with tab_raw:
        st.text_area("Extracted Document Text", res["raw_text"], height=320)

    # Export Buttons
    st.divider()
    col_dl1, col_dl2 = st.columns(2)
    col_dl1.download_button(
        "Download JSON Audit Report",
        data=json.dumps(res, indent=2),
        file_name="gamma4_fact_check_report.json",
        mime="application/json",
        use_container_width=True
    )
    # CSV
    csv_rows = []
    for c in res["claims"]:
        csv_rows.append({
            "Claim ID": c["id"],
            "Original Claim": c["claim_text"],
            "Verdict": c["verdict"],
            "Confidence": c["confidence"],
            "Ground Truth": c["real_fact"],
            "Explanation": c["explanation"],
            "Sources": "; ".join(c.get("sources", []))
        })
    df = pd.DataFrame(csv_rows)
    col_dl2.download_button(
        "Download CSV Audit Report",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name="gamma4_fact_check_report.csv",
        mime="text/csv",
        use_container_width=True
    )
else:
    st.info("👆 Upload any PDF or click **'⚠️ Trap Doc'** in the sidebar to evaluate the assessment document with intentional lies and outdated statistics.")
