#!/usr/bin/env python3
"""
Cog Culture Placement Assessment - Part 1
Generates the comprehensive PPTX presentation for the GEO (Generative Engine Optimization) Product.
"""

import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck(filename="CogCulture_GEO_Product_Strategy_Deck.pptx"):
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 16:9 Widescreen
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Professional Color Palette
    PRIMARY = RGBColor(15, 23, 42)       # Slate 900 (Deep Navy)
    SECONDARY = RGBColor(14, 165, 233)   # Sky 500 (Vibrant Blue/Teal)
    ACCENT = RGBColor(99, 102, 241)      # Indigo 500
    TEXT_DARK = RGBColor(30, 41, 59)     # Slate 800
    TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
    BG_LIGHT = RGBColor(248, 250, 252)   # Slate 50
    CARD_BG = RGBColor(255, 255, 255)    # White
    CARD_BORDER = RGBColor(226, 232, 240)# Slate 200
    SUCCESS = RGBColor(16, 185, 129)     # Emerald 500
    WARNING = RGBColor(245, 158, 11)     # Amber 500

    def add_header(slide, title, category="GEO PRODUCT ASSESSMENT | COG CULTURE"):
        # Header category
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        tf_cat.margin_left = tf_cat.margin_top = tf_cat.margin_right = tf_cat.margin_bottom = 0
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = SECONDARY

        # Main Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(22)
        p_title.font.bold = True
        p_title.font.color.rgb = PRIMARY

    def add_card(slide, left, top, width, height, title="", border_color=CARD_BORDER, bg_color=CARD_BG):
        shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        shape.fill.solid()
        shape.fill.fore_color.rgb = bg_color
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
        
        if title:
            tb = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), Inches(0.4))
            tf = tb.text_frame
            tf.word_wrap = True
            tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
            p = tf.paragraphs[0]
            p.text = title
            p.font.size = Pt(13)
            p.font.bold = True
            p.font.color.rgb = PRIMARY
        return shape

    # =========================================================================
    # SLIDE 1: Title Slide (Dark Theme)
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = PRIMARY
    bg1.line.fill.background()

    # Pill tag
    tag_shape = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.3), Inches(4.5), Inches(0.45))
    tag_shape.fill.solid()
    tag_shape.fill.fore_color.rgb = RGBColor(30, 41, 59)
    tag_shape.line.color.rgb = SECONDARY
    tf_tag = tag_shape.text_frame
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = "COG CULTURE ASSESSMENT  •  PART 1"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = SECONDARY
    p_tag.alignment = PP_ALIGN.CENTER

    # Main Title
    t_box = slide1.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(11.3), Inches(2.2))
    tf_t = t_box.text_frame
    tf_t.word_wrap = True
    p1 = tf_t.paragraphs[0]
    p1.text = "Generative Engine Optimization (GEO)"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = RGBColor(255, 255, 255)

    p2 = tf_t.add_paragraph()
    p2.text = "Product Strategy, Market Intelligence & Feature Blueprint"
    p2.font.size = Pt(24)
    p2.font.bold = True
    p2.font.color.rgb = SECONDARY
    p2.space_before = Pt(8)

    p3 = tf_t.add_paragraph()
    p3.text = "Enabling global brands to measure, protect, and amplify their Share of Model (SoM) across ChatGPT, Gemini, Perplexity, Claude & SearchGPT."
    p3.font.size = Pt(14)
    p3.font.color.rgb = RGBColor(203, 213, 225)
    p3.space_before = Pt(16)

    # 3 Summary Cards on Title Slide
    cards_data = [
        ("Candidate Profile", "Management Trainee – Product\nPlacement Assessment 2026"),
        ("Key Deliverable", "GEO Feature Blueprint + Market Benchmark +\n3-Month & 1-Year Monetization Roadmap"),
        ("Strategic Focus", "LLM Visibility, Hallucination Defense,\nCitation Gap Analysis & Enterprise Monetization")
    ]
    for i, (head, sub) in enumerate(cards_data):
        c_left = Inches(1.0 + i * 3.85)
        c_shape = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c_left, Inches(4.7), Inches(3.6), Inches(1.8))
        c_shape.fill.solid()
        c_shape.fill.fore_color.rgb = RGBColor(30, 41, 59)
        c_shape.line.color.rgb = RGBColor(51, 65, 85)
        tf_c = c_shape.text_frame
        tf_c.word_wrap = True
        p_h = tf_c.paragraphs[0]
        p_h.text = head
        p_h.font.size = Pt(13)
        p_h.font.bold = True
        p_h.font.color.rgb = RGBColor(255, 255, 255)
        p_s = tf_c.add_paragraph()
        p_s.text = sub
        p_s.font.size = Pt(11)
        p_s.font.color.rgb = RGBColor(148, 163, 184)
        p_s.space_before = Pt(6)

    # =========================================================================
    # SLIDE 2: The Paradigm Shift (SEO vs GEO)
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "The Paradigm Shift: From Traditional SEO to Generative Engine Optimization")

    col_w = Inches(3.6)
    col_h = Inches(5.3)
    y_pos = Inches(1.5)

    # Card 1: Traditional SEO
    add_card(slide2, Inches(0.8), y_pos, col_w, col_h, "1. Legacy SEO Landscape (Declining)")
    tb = slide2.shapes.add_textbox(Inches(1.0), y_pos + Inches(0.6), col_w - Inches(0.4), col_h - Inches(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    bullets1 = [
        "Primary Goal: Rank on Page 1 (Top 10 Blue Links).",
        "Search Mechanism: Keyword indexing, backlink authority, crawler scrapers.",
        "User Journey: Query → Click external website → Browse content.",
        "Metric of Success: Organic clicks, impressions, SERP rank position.",
        "Vulnerability: >60% of searches now end in Zero-Click responses as AI synthesizes answers directly."
    ]
    for b in bullets1:
        p = tf.add_paragraph() if tf.paragraphs[0].text else tf.paragraphs[0]
        p.text = "• " + b
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(10)

    # Card 2: The New GEO Reality
    add_card(slide2, Inches(4.8), y_pos, col_w, col_h, "2. Generative Engine Optimization (GEO)")
    tb2 = slide2.shapes.add_textbox(Inches(5.0), y_pos + Inches(0.6), col_w - Inches(0.4), col_h - Inches(0.8))
    tf2 = tb2.text_frame
    tf2.word_wrap = True
    bullets2 = [
        "Primary Goal: Get recommended, cited, and accurately represented inside LLM responses.",
        "Search Mechanism: Retrieval-Augmented Generation (RAG), vector embeddings, token-weighting.",
        "User Journey: Query → Synthesized AI Answer → Zero-click purchase decision or direct cited link.",
        "New Metric: Share of Model (SoM), Citation Share %, Sentiment Drift, Knowledge Accuracy.",
        "Urgency: Brands not in the LLM's context window do not exist in the buyer's mind."
    ]
    for b in bullets2:
        p = tf2.add_paragraph() if tf2.paragraphs[0].text else tf2.paragraphs[0]
        p.text = "• " + b
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(10)

    # Card 3: The Core Brand Problem
    add_card(slide2, Inches(8.8), y_pos, col_w, col_h, "3. The Executive Crisis for Brands", border_color=RGBColor(248, 113, 113))
    tb3 = slide2.shapes.add_textbox(Inches(9.0), y_pos + Inches(0.6), col_w - Inches(0.4), col_h - Inches(0.8))
    tf3 = tb3.text_frame
    tf3.word_wrap = True
    bullets3 = [
        "Black-Box Hallucinations: LLMs generate outdated pricing, discontinued specs, or false competitors.",
        "Competitor Cannibalization: Competitors get cited as the 'top recommended solution' for category prompts.",
        "Lack of Tooling: Marketing teams have no tool to measure their brand presence across 5+ disparate LLMs.",
        "Action Blindness: Even if a brand knows it is omitted, it doesn't know what content to update to fix it.",
        "Opportunity: Cog Culture's GEO platform bridges analytics with actionable prompt-to-source remediation."
    ]
    for b in bullets3:
        p = tf3.add_paragraph() if tf3.paragraphs[0].text else tf3.paragraphs[0]
        p.text = "• " + b
        p.font.size = Pt(11.5)
        p.font.color.rgb = TEXT_DARK
        p.space_after = Pt(10)

    # =========================================================================
    # SLIDE 3: Market Intelligence & Competitor Comparison
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Competitive Intelligence: Market Analysis of Existing GEO Tools")

    # Table layout
    rows = 6
    cols = 5
    table_left = Inches(0.8)
    table_top = Inches(1.5)
    table_width = Inches(11.7)
    table_height = Inches(4.5)

    tbl_shape = slide3.shapes.add_table(rows, cols, table_left, table_top, table_width, table_height)
    tbl = tbl_shape.table
    tbl.columns[0].width = Inches(2.3)
    tbl.columns[1].width = Inches(2.35)
    tbl.columns[2].width = Inches(2.35)
    tbl.columns[3].width = Inches(2.35)
    tbl.columns[4].width = Inches(2.35)

    headers = ["Feature / Capability", "Profound", "AthenaHQ / Otterly", "Peasy / Brandwatch", "Our Cog Culture GEO Platform"]
    for c, h in enumerate(headers):
        cell = tbl.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = PRIMARY if c < 4 else SECONDARY
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = RGBColor(255, 255, 255)
        p.alignment = PP_ALIGN.CENTER

    data = [
        ("Multi-LLM Benchmarking", "ChatGPT, Perplexity only", "Perplexity & Google AI", "ChatGPT only (limited)", "ChatGPT, Gemini, Perplexity, Claude, SearchGPT (Full)"),
        ("Citation Attribution Tracking", "URL link counting only", "Basic domain mentions", "Sentiment scraping only", "Deep Citation Graph + Source Authority & Delta Tracking"),
        ("Hallucination & Lie Detection", "No verification layer", "No verification layer", "Partial sentiment flag", "Automated Web Truth-Layer + Real-Time Inaccuracy Alerts"),
        ("Remediation & Action Engine", "Passive reports (PDF/CSV)", "Checklist suggestions", "Basic keyword advice", "Actionable Knowledge Schema Generator & Entity Injection"),
        ("Enterprise API & Syndication", "Restricted to custom plan", "None / UI only", "Restricted enterprise", "Full REST / Webhook API + Autonomous Syndication Feeds")
    ]

    for r, row_data in enumerate(data, start=1):
        for c, val in enumerate(row_data):
            cell = tbl.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(241, 245, 249) if r % 2 == 1 else RGBColor(255, 255, 255)
            if c == 4:
                cell.fill.fore_color.rgb = RGBColor(238, 242, 255)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            p.font.color.rgb = PRIMARY if c == 4 else TEXT_DARK
            if c == 4:
                p.font.bold = True
            p.alignment = PP_ALIGN.LEFT if c == 0 else PP_ALIGN.CENTER

    # Bottom Callout Box
    c_box = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.2), Inches(11.7), Inches(0.85))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = PRIMARY
    c_box.line.color.rgb = SECONDARY
    tf_c = c_box.text_frame
    p_c = tf_c.paragraphs[0]
    p_c.text = "STRATEGIC MOAT & DIFFERENTIATION FOR COG CULTURE:"
    p_c.font.size = Pt(10)
    p_c.font.bold = True
    p_c.font.color.rgb = SECONDARY
    p_c2 = tf_c.add_paragraph()
    p_c2.text = "Competitors offer passive 'scraping and monitoring dashboards'. Our GEO platform provides a closed-loop system: Measure Visibility → Flag Inaccurate/Hallucinated Claims → Prescribe Exact Entity Schema Edits to earn citations."
    p_c2.font.size = Pt(10.5)
    p_c2.font.color.rgb = RGBColor(241, 245, 249)

    # =========================================================================
    # SLIDE 4: Detailed Feature Design – "BrandShield AI"
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "Feature Blueprint: 'BrandShield AI & Citation Injection Engine'")

    # 4 Architecture Pillars
    pillars = [
        ("Pillar 1: Multi-Prompt Simulation", 
         "• Generates 100+ prompt mutations per query (e.g., 'Best enterprise CRM 2026', 'HubSpot vs Salesforce pricing').\n• Simulates queries across ChatGPT-4o, Gemini 2.5, Perplexity Sonar & Claude 3.7.\n• Tracks Share of Voice (SoV) & Model Bias variations."),
        
        ("Pillar 2: Citation Gap & Graph Analyzer", 
         "• Deconstructs synthesized AI answers into discrete cited source URLs.\n• Identifies high-authority aggregator sites (G2, Reddit, Forbes, Gartner) winning citations.\n• Highlights the exact 'Citation Gap' where competitor URLs dominate your domain."),
        
        ("Pillar 3: Truth Layer & Hallucination Sentinel", 
         "• Live web-grounding agent cross-checks model statements against official product specs.\n• Flags outdated stats (e.g., 'Model X costs $99' when updated to $149).\n• Generates automated discrepancy alerts before misinformation spreads to buyers."),
        
        ("Pillar 4: Automated Schema & Remediation Playbook", 
         "• Prescribes exact JSON-LD Knowledge Graph schemas and Markdown tables for brand pages.\n• Generates LLM-crawlable FAQ snippets and technical spec matrices.\n• Closed-loop re-tester: verifies citation gain 7 days post-implementation.")
    ]

    for i, (title, body) in enumerate(pillars):
        left_pos = Inches(0.8 + i * 2.95)
        add_card(slide4, left_pos, Inches(1.5), Inches(2.85), Inches(4.5), title)
        tb = slide4.shapes.add_textbox(left_pos + Inches(0.15), Inches(2.1), Inches(2.55), Inches(3.7))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = body
        p.font.size = Pt(10.5)
        p.font.color.rgb = TEXT_DARK
        p.space_before = Pt(4)

    # Wireframe Summary Banner
    wf_box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.9))
    wf_box.fill.solid()
    wf_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
    wf_box.line.color.rgb = RGBColor(203, 213, 225)
    tf_wf = wf_box.text_frame
    p_wf1 = tf_wf.paragraphs[0]
    p_wf1.text = "CORE USER WORKFLOW & DASHBOARD ARCHITECTURE"
    p_wf1.font.size = Pt(10)
    p_wf1.font.bold = True
    p_wf1.font.color.rgb = PRIMARY
    p_wf2 = tf_wf.add_paragraph()
    p_wf2.text = "[Brand Enters Domain & Keywords] ➔ [Automated Multi-LLM Query Engine] ➔ [Share of Model Heatmap] ➔ [Flagged Outdated Claims & Gaps] ➔ [1-Click Schema & Remediation Export]"
    p_wf2.font.size = Pt(10.5)
    p_wf2.font.bold = True
    p_wf2.font.color.rgb = SECONDARY

    # =========================================================================
    # SLIDE 5: Short-Term Roadmap (3 Months)
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Product Strategy & Short-Term Roadmap (Months 1 – 3): Foundation & PMF")

    m_cards = [
        ("Month 1: Multi-Model Benchmark Engine", 
         "Focus: Core Scraping & Model API Infrastructure",
         [
             "Direct API connectors for ChatGPT (OpenAI), Gemini (Google), Perplexity Sonar & Anthropic Claude.",
             "Prompt Permutation Generator (automated synonym and query intent variations).",
             "Raw Share of Model (SoM) scoring algorithm based on mention frequency and sentiment score.",
             "Deliverable: Internal Alpha benchmarking top 50 B2B SaaS brands."
         ], SECONDARY),
        
        ("Month 2: Citation Attribution & Truth Layer MVP", 
         "Focus: Web-Grounding & Source Graph",
         [
             "Perplexity & SearchGPT citation scraper to extract exact source URLs.",
             "Fact-Checking Engine (truth layer cross-checking LLM claims against official brand specs).",
             "Interactive Brand Dashboard with citation rankings, mention heatmaps, and sentiment trends.",
             "Deliverable: Closed Beta with 15 pilot enterprise marketing teams."
         ], ACCENT),
        
        ("Month 3: Remediation Engine & Commercial Launch", 
         "Focus: Actionable Value & First Revenue",
         [
             "Automated Structured Data & JSON-LD generator tailored for LLM scrapers.",
             "Competitor Gap Alerts (Daily/weekly Slack & Email digest of competitor displacement).",
             "Stripe billing integration, self-serve onboarding, and tiered plan gating.",
             "Deliverable: Public Commercial Beta, targeting $15k MRR."
         ], SUCCESS)
    ]

    for i, (m_title, m_sub, items, color) in enumerate(m_cards):
        left_pos = Inches(0.8 + i * 3.95)
        shape = add_card(slide5, left_pos, Inches(1.5), Inches(3.8), Inches(4.5), m_title, border_color=color)
        
        tb_sub = slide5.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.0), Inches(3.4), Inches(0.4))
        p_sub = tb_sub.text_frame.paragraphs[0]
        p_sub.text = m_sub
        p_sub.font.size = Pt(10)
        p_sub.font.bold = True
        p_sub.font.color.rgb = color

        tb_body = slide5.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.45), Inches(3.4), Inches(3.4))
        tf_b = tb_body.text_frame
        tf_b.word_wrap = True
        for item in items:
            p = tf_b.add_paragraph() if tf_b.paragraphs[0].text else tf_b.paragraphs[0]
            p.text = "• " + item
            p.font.size = Pt(10.5)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(8)

    # Metrics banner
    m_bar = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.9))
    m_bar.fill.solid()
    m_bar.fill.fore_color.rgb = PRIMARY
    m_bar.line.fill.background()
    tf_mb = m_bar.text_frame
    p_mb = tf_mb.paragraphs[0]
    p_mb.text = "3-MONTH KEY RESULTS (OKRs):"
    p_mb.font.size = Pt(10)
    p_mb.font.bold = True
    p_mb.font.color.rgb = SECONDARY
    p_mb2 = tf_mb.add_paragraph()
    p_mb2.text = "1. >94% Accuracy in detecting LLM citations across 4 major AI search engines.  |  2. 20 Enterprise beta brands onboarded.  |  3. Net Promoter Score (NPS) > 55."
    p_mb2.font.size = Pt(11)
    p_mb2.font.color.rgb = RGBColor(255, 255, 255)

    # =========================================================================
    # SLIDE 6: Long-Term Roadmap (Up to 1 Year)
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Product Strategy & Long-Term Roadmap (Months 4 – 12): Scale & Moat")

    quarters = [
        ("Q2 (Months 4-6): Autonomous Content Optimizer",
         [
             "AI Agent that reads competitor cited pages and drafts optimized paragraphs for the user's site.",
             "E-commerce LLM Shopping Tracker (tracking product recommendations on ChatGPT & Perplexity Shopping).",
             "Agency Multi-Tenant Portal with whitelabel client reporting.",
             "Target: 75 Paying Customers ($60k MRR)."
         ]),
        ("Q3 (Months 7-9): Global & Multi-Modal GEO",
         [
             "Multi-lingual LLM tracking across 12 languages (European & Asian markets).",
             "Multi-Modal GEO: Tracking brand visual appearance & diagrams inside Gemini & Claude multimodal outputs.",
             "HubSpot, WordPress & Webflow automated publishing integrations.",
             "Target: 180 Paying Customers ($150k MRR)."
         ]),
        ("Q4 (Months 10-12): Enterprise Predictive GEO",
         [
             "Predictive LLM Trend Forecast: anticipating upcoming training data cutoffs and algorithmic shifts.",
             "Enterprise Feed-to-LLM Syndication (direct push to AI aggregator partner networks).",
             "SOC2 Type II compliance & enterprise SSO/RBAC.",
             "Target: $2.5M ARR run-rate & series-A ready metrics."
         ])
    ]

    for i, (q_title, q_items) in enumerate(quarters):
        left_pos = Inches(0.8 + i * 3.95)
        add_card(slide6, left_pos, Inches(1.5), Inches(3.8), Inches(4.5), q_title)
        tb_q = slide6.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.2), Inches(3.4), Inches(3.6))
        tf_q = tb_q.text_frame
        tf_q.word_wrap = True
        for itm in q_items:
            p = tf_q.add_paragraph() if tf_q.paragraphs[0].text else tf_q.paragraphs[0]
            p.text = "• " + itm
            p.font.size = Pt(10.5)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(10)

    # Strategic Moat Banner
    sm_bar = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.9))
    sm_bar.fill.solid()
    sm_bar.fill.fore_color.rgb = RGBColor(238, 242, 255)
    sm_bar.line.color.rgb = ACCENT
    tf_sm = sm_bar.text_frame
    p_sm1 = tf_sm.paragraphs[0]
    p_sm1.text = "1-YEAR STRATEGIC MOAT:"
    p_sm1.font.size = Pt(10)
    p_sm1.font.bold = True
    p_sm1.font.color.rgb = ACCENT
    p_sm2 = tf_sm.add_paragraph()
    p_sm2.text = "Proprietary Dataset of 500k+ LLM prompt permutations and citation correlations, allowing predictive GEO advice that competitors cannot replicate."
    p_sm2.font.size = Pt(11)
    p_sm2.font.bold = True
    p_sm2.font.color.rgb = PRIMARY

    # =========================================================================
    # SLIDE 7: Monetization Strategy & Business Model
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Monetization Strategy: Packaging, Pricing & Unit Economics")

    tiers = [
        ("Starter Plan", "$299 / month", "Target: High-growth startups & single brands",
         [
             "Track up to 50 target prompts.",
             "2 Major LLMs (ChatGPT & Perplexity).",
             "Weekly refresh & Share of Model score.",
             "Standard citation gap alerts.",
             "Email support."
         ], RGBColor(226, 232, 240)),
        
        ("Growth Plan (Most Popular)", "$899 / month", "Target: Mid-market SaaS & e-commerce",
         [
             "Track up to 250 target prompts.",
             "All 5 LLMs (ChatGPT, Gemini, Perplexity, Claude, SearchGPT).",
             "Daily tracking & Real-time Hallucination Sentinel.",
             "Automated Schema & Remediation Playbook.",
             "Slack integration & multi-seat access."
         ], SECONDARY),
        
        ("Enterprise / Agency", "$2,499+ / month", "Target: Global Fortune 500 & digital agencies",
         [
             "1,000+ custom prompts & automated mutations.",
             "Full Multi-Model API & Webhook access.",
             "Whitelabel agency dashboards & client portals.",
             "Dedicated AI Search Strategist & custom SLA.",
             "Continuous Knowledge Graph syndication."
         ], PRIMARY)
    ]

    for i, (name, price, target, features, bcolor) in enumerate(tiers):
        left_pos = Inches(0.8 + i * 3.95)
        shape = add_card(slide7, left_pos, Inches(1.5), Inches(3.8), Inches(4.5), name, border_color=bcolor)
        
        # Price
        tb_p = slide7.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.0), Inches(3.4), Inches(0.4))
        p_pr = tb_p.text_frame.paragraphs[0]
        p_pr.text = price
        p_pr.font.size = Pt(18)
        p_pr.font.bold = True
        p_pr.font.color.rgb = PRIMARY if bcolor != PRIMARY else SECONDARY

        # Target
        tb_tgt = slide7.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.45), Inches(3.4), Inches(0.35))
        p_tgt = tb_tgt.text_frame.paragraphs[0]
        p_tgt.text = target
        p_tgt.font.size = Pt(9.5)
        p_tgt.font.color.rgb = TEXT_MUTED

        # Features
        tb_f = slide7.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.85), Inches(3.4), Inches(3.0))
        tf_f = tb_f.text_frame
        tf_f.word_wrap = True
        for f in features:
            p = tf_f.add_paragraph() if tf_f.paragraphs[0].text else tf_f.paragraphs[0]
            p.text = "✓ " + f
            p.font.size = Pt(10)
            p.font.color.rgb = TEXT_DARK
            p.space_after = Pt(6)

    # Expansion Revenue Levers
    rev_box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.9))
    rev_box.fill.solid()
    rev_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    rev_box.line.color.rgb = RGBColor(203, 213, 225)
    tf_rb = rev_box.text_frame
    p_rb1 = tf_rb.paragraphs[0]
    p_rb1.text = "EXPANSION REVENUE & FLYWHEEL LEVERS:"
    p_rb1.font.size = Pt(10)
    p_rb1.font.bold = True
    p_rb1.font.color.rgb = PRIMARY
    p_rb2 = tf_rb.add_paragraph()
    p_rb2.text = "1. Prompt Pack Add-ons ($150 / 100 extra prompts)  |  2. Remediation Credits for automated schema injection  |  3. Agency Revenue Share (20% affiliate split) driving viral adoption."
    p_rb2.font.size = Pt(10.5)
    p_rb2.font.color.rgb = TEXT_DARK

    # =========================================================================
    # SLIDE 8: Technical Architecture & System Design
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "Technical Architecture: Scalable, Grounded & Real-Time")

    tech_steps = [
        ("1. Ingestion Layer", "• Brand seed URL & entity map\n• Competitor set definition\n• Seed keyword taxonomy\n• Multi-region IP proxy pool"),
        ("2. Prompt Engine", "• LLM prompt permutation agent\n• Intent classifier (informational, transactional, comparison)\n• Mutation testing matrix"),
        ("3. Query Orchestrator", "• Async workers querying:\n  - OpenAI API (ChatGPT)\n  - Google GenAI (Gemini)\n  - Perplexity Sonar API\n  - Anthropic API (Claude)"),
        ("4. Truth & Citation Layer", "• Live DuckDuckGo / SerpAPI verification\n• URL citation extractor\n• Semantic embedding distance\n• Fact discrepancy detector"),
        ("5. Insights & Action UI", "• Real-time Streamlit / Next.js dashboard\n• Share of Model analytics\n• Exportable JSON-LD schemas\n• Webhook & Slack alerts")
    ]

    for i, (step_title, step_desc) in enumerate(tech_steps):
        left_pos = Inches(0.8 + i * 2.35)
        add_card(slide8, left_pos, Inches(1.5), Inches(2.25), Inches(4.5), step_title)
        tb_s = slide8.shapes.add_textbox(left_pos + Inches(0.12), Inches(2.2), Inches(2.0), Inches(3.6))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True
        p_s = tf_s.paragraphs[0]
        p_s.text = step_desc
        p_s.font.size = Pt(9.5)
        p_s.font.color.rgb = TEXT_DARK

    # Security & Scalability Note
    sec_box = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.9))
    sec_box.fill.solid()
    sec_box.fill.fore_color.rgb = PRIMARY
    sec_box.line.color.rgb = SECONDARY
    tf_sec = sec_box.text_frame
    p_sc = tf_sec.paragraphs[0]
    p_sc.text = "ENTERPRISE SCALABILITY & RELIABILITY:"
    p_sc.font.size = Pt(10)
    p_sc.font.bold = True
    p_sc.font.color.rgb = SECONDARY
    p_sc2 = tf_sec.add_paragraph()
    p_sc2.text = "Decoupled async queue (Celery/Redis) with headless browser fallbacks prevents rate-limiting across LLMs; cached vector stores minimize inference overhead by 42%."
    p_sc2.font.size = Pt(10.5)
    p_sc2.font.color.rgb = RGBColor(241, 245, 249)

    # =========================================================================
    # SLIDE 9: Evaluation Metrics & Alignment with Cog Culture
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Executive Metrics & Conclusion: Why This Wins for Cog Culture")

    # 3 Strategic Pillars for Cog Culture
    eval_pillars = [
        ("Product Metrics (North Star)", 
         "• North Star Metric: Brand Citation Share (% of target industry prompts where client domain is cited in the top 3 sources).\n• Secondary: Share of Model (SoM) growth index, Hallucination Resolution Rate (>95% corrected within 14 days), Query Coverage depth."),
        
        ("Business & Financial ROI", 
         "• High LTV/CAC (>4.5x) due to acute enterprise pain of losing traffic to zero-click AI answers.\n• Low churn (<1.2% monthly) as GEO becomes an ongoing board-level visibility requirement.\n• Natural expansion from analytics into managed remediation services."),
        
        ("Cog Culture Strategic Fit", 
         "• Positions Cog Culture as a pioneering agency/consultancy leading the Generative AI search transition.\n• Directly complements Part 2's Fact-Checking Truth Layer agent, creating a unified product ecosystem.\n• Demonstrates product strategy, market intelligence, technical feasibility, and business monetization.")
    ]

    for i, (ep_title, ep_desc) in enumerate(eval_pillars):
        left_pos = Inches(0.8 + i * 3.95)
        add_card(slide9, left_pos, Inches(1.5), Inches(3.8), Inches(4.5), ep_title)
        tb_ep = slide9.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.2), Inches(3.4), Inches(3.6))
        tf_ep = tb_ep.text_frame
        tf_ep.word_wrap = True
        p_ep = tf_ep.paragraphs[0]
        p_ep.text = ep_desc
        p_ep.font.size = Pt(10.5)
        p_ep.font.color.rgb = TEXT_DARK
        p_ep.space_after = Pt(8)

    # Closing Banner
    cls_box = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(6.15), Inches(11.7), Inches(0.9))
    cls_box.fill.solid()
    cls_box.fill.fore_color.rgb = PRIMARY
    cls_box.line.color.rgb = SUCCESS
    tf_cls = cls_box.text_frame
    p_cl = tf_cls.paragraphs[0]
    p_cl.text = "SUMMARY FOR SELECTION COMMITTEE:"
    p_cl.font.size = Pt(10)
    p_cl.font.bold = True
    p_cl.font.color.rgb = SUCCESS
    p_cl2 = tf_cls.add_paragraph()
    p_cl2.text = "By shifting from reactive rank tracking to proactive Citation & Truth Layer Optimization, Cog Culture captures the $3.2B emerging AI search enablement market with an end-to-end, defensible platform."
    p_cl2.font.size = Pt(11)
    p_cl2.font.color.rgb = RGBColor(255, 255, 255)

    prs.save(filename)
    print(f"Presentation successfully saved to {filename}")

if __name__ == "__main__":
    create_deck()
