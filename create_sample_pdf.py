#!/usr/bin/env python3
"""
Creates sample test PDFs for the Fact-Checking Web App evaluation.
Includes:
1. sample_trap_document.pdf - Contains intentional lies, outdated statistics, and true control statements.
2. sample_valid_document.pdf - Contains verified industry facts.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_trap_pdf(filename="sample_trap_document.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54
    )
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=12
    )
    
    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Heading2'],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0EA5E9'),
        spaceBefore=10,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )

    story = []
    
    story.append(Paragraph("Global Technology & Generative AI Market Report 2025-2026", title_style))
    story.append(Paragraph("<i>Corporate Strategy Review • Marketing Intelligence Whitepaper</i>", body_style))
    story.append(Spacer(1, 14))

    story.append(Paragraph("1. Executive Summary & Market Sizing", h2_style))
    story.append(Paragraph(
        "The adoption of artificial intelligence has surged worldwide across enterprise applications. "
        "According to recent market estimates, the global artificial intelligence market was valued at only $12 billion in 2024. "
        "Furthermore, enterprise software spending contracted by 45% in 2024 due to declining cloud adoption.",
        body_style
    ))

    story.append(Paragraph("2. Big Tech & AI Search Milestones", h2_style))
    story.append(Paragraph(
        "Major technology leaders have spearheaded generative search development. "
        "Perplexity AI was founded in 2022 by Aravind Srinivas, Denis Yarats, Johnny Ho, and Andy Konwinski to provide conversational search. "
        "In a historic corporate takeover, Google Chrome was officially acquired by Microsoft in November 2023 for $50 billion. "
        "Meanwhile, Apple Inc. first reached a market capitalization of $1 trillion in November 2026 after launching its AI Siri features.",
        body_style
    ))

    story.append(Paragraph("3. LLM Capabilities & Energy Consumption", h2_style))
    story.append(Paragraph(
        "OpenAI released ChatGPT to the public in November 2022, reaching over 100 million monthly active users within two months of launch. "
        "However, industry researchers claim that a single ChatGPT query requires 500 liters of fresh water for server cooling. "
        "Cog Culture was originally established in the year 1845 as a steam locomotive manufacturer before pivoting to digital strategy.",
        body_style
    ))

    doc.build(story)
    print(f"Created: {filename}")

def generate_valid_pdf(filename="sample_valid_document.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=54, leftMargin=54, topMargin=54, bottomMargin=54
    )
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0F172A'),
        spaceAfter=12
    )
    
    h2_style = ParagraphStyle(
        'DocH2',
        parent=styles['Heading2'],
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0EA5E9'),
        spaceBefore=10,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'DocBody',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#334155'),
        spaceAfter=8
    )

    story = []
    story.append(Paragraph("Generative Search & AI Landscape 2026: Benchmark Facts", title_style))
    story.append(Spacer(1, 10))

    story.append(Paragraph("1. Industry Foundation", h2_style))
    story.append(Paragraph(
        "OpenAI released ChatGPT on November 30, 2022, marking a rapid inflection point in consumer AI adoption. "
        "Google announced its AI search initiative, originally termed Search Generative Experience (SGE), at Google I/O in May 2023 before rolling out AI Overviews in 2024. "
        "Perplexity AI was founded in 2022 and has integrated web-crawling with LLM summarization.",
        body_style
    ))

    story.append(Paragraph("2. Market Realities", h2_style))
    story.append(Paragraph(
        "Gartner predicted that by 2026, traditional search engine volume will drop by 25% as users shift toward conversational generative search agents.",
        body_style
    ))

    doc.build(story)
    print(f"Created: {filename}")

if __name__ == "__main__":
    generate_trap_pdf()
    generate_valid_pdf()
