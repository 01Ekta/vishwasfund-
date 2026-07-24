# Architecture

```
Frontend (React + Tailwind)
        │
        ▼
Backend API (Python / FastAPI)
        │
        ▼
Intelligence Layer
  ├─ scikit-learn eligibility model (approval-likelihood scoring)
  └─ Google Gemini API (voice input, vernacular language understanding)
        │
        ▼
Data & Hosting
  ├─ Firebase Firestore (data) + Firebase Auth (login)
  └─ Google Cloud Run (deployment)
```

## Data flow

1. **User onboarding** — voice or text, in any supported regional language.
2. **Eligibility ML engine** — scores each scheme by approval likelihood, not just static eligibility.
3. **Trust verification** — checks lender & mentor govt registration details.
4. **Ranked matches** — schemes, mentors & lenders returned best-fit first.
5. **Dashboard** — track applications & upcoming mentor sessions.

See the pitch deck (`docs/` or team drive) for the full problem statement and solution writeup.
