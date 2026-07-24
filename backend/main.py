"""
VishwasFund backend — FastAPI service.

Exposes endpoints for:
- eligibility matching (delegates to ml/ scoring model)
- lender/mentor verification lookup
- basic profile + dashboard data
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="VishwasFund API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten before real deployment
    allow_methods=["*"],
    allow_headers=["*"],
)


class BusinessProfile(BaseModel):
    business_type: str
    location: str
    monthly_income: float
    existing_assets: bool = False
    prior_loan_history: bool = False


@app.get("/")
def root():
    return {"status": "ok", "service": "VishwasFund API"}


@app.post("/match")
def match_schemes(profile: BusinessProfile):
    """
    Placeholder endpoint — will call the trained model in ml/eligibility_model.py
    and return a ranked list of schemes + mentors + verified lenders.
    """
    return {
        "matches": [
            {"name": "Mudra Yojana — Shishu Loan", "type": "scheme", "match_score": 0.0},
            {"name": "Example Mentor", "type": "mentor", "match_score": 0.0},
        ],
        "note": "stub response — connect ml/eligibility_model.py for real scoring",
    }


@app.get("/verify/{entity_id}")
def verify_entity(entity_id: str):
    """Placeholder for the trust/verification layer lookup."""
    return {"entity_id": entity_id, "verified": False, "note": "stub — connect real registry lookup"}
