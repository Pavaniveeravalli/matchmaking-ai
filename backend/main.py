from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- USER MODEL ----------
class UserProfile(BaseModel):
    role: str
    industry: str
    stage: str
    geography: str


# ---------- MATCH ROUTE ----------
@app.post("/matches")
def get_matches(user: UserProfile):

    all_profiles = [
        {
            "name": "Aisha Khan",
            "role": "Founder",
            "industry": "B2B SaaS",
            "stage": "Seed",
            "geography": "MENA",
            "score": 87
        },
        {
            "name": "Marcus Chen",
            "role": "Investor",
            "industry": "FinTech",
            "stage": "Series A",
            "geography": "SEA",
            "score": 92
        },
        {
            "name": "Elena Rodriguez",
            "role": "Mentor",
            "industry": "Enterprise",
            "stage": "Growth",
            "geography": "North America",
            "score": 78
        },
        {
            "name": "David Okonkwo",
            "role": "Founder",
            "industry": "HealthTech",
            "stage": "Pre-seed",
            "geography": "Africa",
            "score": 84
        }
    ]

    # -------- SMART ROLE MATCHING --------
    if user.role == "Founder":
        filtered = [p for p in all_profiles if p["role"] == "Investor"]
    elif user.role == "Investor":
        filtered = [p for p in all_profiles if p["role"] == "Founder"]
    elif user.role == "Mentor":
        filtered = [p for p in all_profiles if p["role"] == "Founder"]
    else:
        filtered = all_profiles

    if not filtered:
        filtered = all_profiles

    import random
    selected = random.choice(filtered)

    return {
        "match": {
            "name": selected["name"],
            "role": selected["role"],
            "tags": [
                selected["industry"],
                selected["stage"],
                selected["geography"]
            ],
            "score": selected["score"]
        },
        "reason": {
            "text": f"Matched because you are a {user.role} and they are a {selected['role']} in related ecosystem.",
            "factors": [
                selected["industry"],
                selected["stage"],
                selected["geography"]
            ]
        },
        "actions": [
            {"type": "requestDeck", "label": "Request Deck", "primary": True},
            {"type": "bookCall", "label": "Book Call", "primary": False},
            {"type": "follow", "label": "Follow", "primary": False}
        ]
    }



# ---------- STATIC FILES ----------
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def read_index():
    return FileResponse(os.path.join("../frontend", "index.html"))
