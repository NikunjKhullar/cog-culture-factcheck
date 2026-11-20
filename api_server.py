"""
FastAPI Server providing API Endpoints for Gamma 4 (31B) and External LLMs
to access the internet for cross-checking data validity against government websites
and research papers only, while strictly filtering out social media and unverified third parties.
"""

import os
import re
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException, Query, Body
from pydantic import BaseModel, Field
import fact_checker

app = FastAPI(
    title="FactShield AI - Gamma 4 Live Verification & Search API",
    description="Dedicated API endpoint enabling Gamma 4 (31B) to access live web data restricted to government websites and academic research papers.",
    version="2.0.0"
)

class SearchRequest(BaseModel):
    query: str = Field(..., description="Fact or statistic to cross-check")
    max_results: int = Field(default=5, description="Number of authoritative sources to retrieve")
    filter_type: str = Field(default="gov_and_research", description="gov_and_research | all_authoritative")

class SearchResultItem(BaseModel):
    title: str
    snippet: str
    href: str
    source_type: str  # Government (.gov), Research Paper (arxiv/nih/nature), or Authoritative Registry

class SearchResponse(BaseModel):
    query: str
    total_found: int
    sources: List[SearchResultItem]
    filtered_out_social_media: bool = True

class VerifyClaimRequest(BaseModel):
    claim_text: str = Field(..., description="Stated claim with figures, dates, or assertions")
    context: Optional[str] = Field(default="", description="Surrounding document context")
    gemma_api_key: Optional[str] = Field(default=None, description="Optional Gemma/Gamma model API key")

class VerifyClaimResponse(BaseModel):
    claim_text: str
    verdict: str  # Verified | Inaccurate | False
    confidence: float
    real_fact: str
    explanation: str
    government_and_research_sources: List[str]

@app.get("/")
def health_check():
    return {
        "status": "online",
        "service": "FactShield AI Gamma 4 Search & Verification API",
        "supported_models": ["Gamma 4:31B", "Gemma 31B", "Sarvam Document Intelligence"],
        "enforced_filters": {
            "allowed_domains": ["Government (*.gov, *.gov.in, *.nic.in, sec.gov, census.gov)", "Research Papers (arXiv, PubMed/NIH, Nature, Science, IEEE, Springer)"],
            "blocked_domains": ["twitter.com", "x.com", "reddit.com", "facebook.com", "instagram.com", "quora.com", "tiktok.com", "medium.com"]
        }
    }

@app.post("/api/search", response_model=SearchResponse)
def search_authoritative_internet(req: SearchRequest):
    """
    API Endpoint that allows Gamma 4 to access the internet for cross-checking data validity,
    strictly restricted to government websites and research papers, excluding social media.
    """
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    raw_results = fact_checker.search_authoritative_web(req.query, max_results=req.max_results)
    
    formatted_sources = []
    for r in raw_results:
        href = r.get("href", "")
        # Classify source type
        if any(g in href for g in [".gov", ".gov.in", ".nic.in", "sec.gov", "census.gov", "bls.gov"]):
            stype = "Government Portal (.gov)"
        elif any(rp in href for rp in ["arxiv.org", "nih.gov", "nature.com", "science.org", "ieee.org", "semanticscholar.org"]):
            stype = "Peer-Reviewed Research Paper"
        else:
            stype = "Authoritative Knowledge Registry"

        formatted_sources.append(SearchResultItem(
            title=r.get("title", ""),
            snippet=r.get("snippet", ""),
            href=href,
            source_type=stype
        ))

    return SearchResponse(
        query=req.query,
        total_found=len(formatted_sources),
        sources=formatted_sources,
        filtered_out_social_media=True
    )

@app.post("/api/verify_claim", response_model=VerifyClaimResponse)
def verify_claim_endpoint(req: VerifyClaimRequest):
    """
    Cross-checks a single claim using Gamma 4 / Gemma 31B and live government/research paper sources.
    """
    claim_dict = {
        "id": 1,
        "claim_text": req.claim_text,
        "category": "statistic",
        "search_query": req.claim_text
    }
    web_results = fact_checker.search_authoritative_web(req.claim_text, max_results=4)
    
    verification = fact_checker.verify_claim_with_gamma4(
        claim_dict,
        web_results,
        gemma_api_key=req.gemma_api_key
    )

    return VerifyClaimResponse(
        claim_text=req.claim_text,
        verdict=verification["verdict"],
        confidence=verification["confidence"],
        real_fact=verification["real_fact"],
        explanation=verification["explanation"],
        government_and_research_sources=verification.get("sources", [])
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server:app", host="127.0.0.1", port=8000, reload=False)
