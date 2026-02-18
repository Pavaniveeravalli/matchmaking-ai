from pydantic import BaseModel
from typing import List

class UserProfile(BaseModel):
    role: str
    industry: str
    stage: str
    geography: str

class MatchProfile(BaseModel):
    name: str
    role: str
    tags: List[str]
    score: int

class MatchReason(BaseModel):
    text: str
    factors: List[str]

class MatchAction(BaseModel):
    type: str
    label: str
    primary: bool
