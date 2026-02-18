from models import MatchProfile

mock_profiles = [
    MatchProfile(name="Aisha Khan", role="Founder", tags=["B2B SaaS", "MENA", "Seed", "AI"], score=87),
    MatchProfile(name="Marcus Chen", role="Investor", tags=["Series A", "FinTech", "Southeast Asia", "$2-5M"], score=92),
    MatchProfile(name="Elena Rodriguez", role="Mentor", tags=["GTM Strategy", "Enterprise Sales", "North America", "Ex-Google"], score=78),
    MatchProfile(name="David Okonkwo", role="Founder", tags=["HealthTech", "Africa", "Pre-seed", "Telemedicine"], score=84),
    MatchProfile(name="Sarah Mitchell", role="Talent", tags=["Full Stack", "React", "Senior", "Remote"], score=91)
]

reason_templates = {
    'Founder-Investor': [
        'You invest in {industry} in {geography} + they match your stage preference',
        'Strong alignment on {industry} focus + their traction fits your thesis',
        'Previous successful bets in {industry} + they have strong unit economics'
    ],
    'Founder-Mentor': [
        'You need {tags} expertise + they have relevant experience',
        'Their background in {industry} matches your current challenges',
        'They helped similar {stage} companies scale successfully'
    ],
    'Investor-Founder': [
        'Their {industry} focus aligns with your thesis + strong team',
        'Compelling {stage} metrics + clear path to Series A',
        'Large market opportunity in {geography} + proven product-market fit'
    ],
    'Founder-Talent': [
        'Their tech stack matches your needs + {stage} experience',
        'Strong {tags} skills + interest in {industry}',
        'Previous success at similar {stage} startups'
    ]
}
