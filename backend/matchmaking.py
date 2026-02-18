from models import MatchProfile, MatchReason, MatchAction, UserProfile

# Mock profiles
mock_profiles = [
    MatchProfile(name="Aisha Khan", role="Founder", tags=["B2B SaaS", "MENA", "Seed", "AI"], score=87),
    MatchProfile(name="Marcus Chen", role="Investor", tags=["Series A", "FinTech", "Southeast Asia", "$2-5M"], score=92),
    MatchProfile(name="Elena Rodriguez", role="Mentor", tags=["GTM Strategy", "Enterprise Sales", "North America", "Ex-Google"], score=78),
    MatchProfile(name="David Okonkwo", role="Founder", tags=["HealthTech", "Africa", "Pre-seed", "Telemedicine"], score=84),
    MatchProfile(name="Sarah Mitchell", role="Talent", tags=["Full Stack", "React", "Senior", "Remote"], score=91),
]

def filter_and_rank_matches(user: UserProfile):
    # For simplicity, return all mock profiles
    return mock_profiles

def generate_reason(user: UserProfile, match: MatchProfile):
    text = f"{match.name} is a {match.role} with tags {', '.join(match.tags)}"
    factors = match.tags[:3]
    return MatchReason(text=text, factors=factors)

def available_actions(user: UserProfile):
    base_actions = [
        MatchAction(type="intro", label="Intro", primary=False),
        MatchAction(type="follow", label="Follow", primary=False)
    ]
    if user.role == "Founder":
        return [
            MatchAction(type="requestDeck", label="Request Deck", primary=True),
            MatchAction(type="bookCall", label="Book Call", primary=False),
            *base_actions
        ]
    elif user.role == "Investor":
        return [
            MatchAction(type="bookCall", label="Book Call", primary=True),
            MatchAction(type="requestDeck", label="Request Deck", primary=False),
            *base_actions
        ]
    else:
        return [
            MatchAction(type="bookCall", label="Book Call", primary=True),
            *base_actions
        ]
