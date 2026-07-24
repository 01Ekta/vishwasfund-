# VishwasFund

**Funding, mentorship & trust for rural and semi-urban women entrepreneurs.**

Built for Hack Days Delhi — Financial Empowerment track (PS22).

## The problem

Women entrepreneurs in villages and small towns can't discover which funding schemes they actually qualify for — information is scattered, English-heavy, and hard to navigate. On top of that, informal lenders and fake "mentors" exploit the trust gap, and formal mentorship rarely reaches beyond urban hubs.

## What we're building

- **Smart Eligibility Engine** — an ML model that ranks government/microfinance schemes by real approval likelihood, not just static eligibility rules.
- **Verified Trust Layer** — lenders and mentors carry a govt-verified badge plus a community trust score, so predatory agents are easy to spot.
- **Vernacular, voice-first access** — onboarding works by voice and in regional languages, so English fluency is never a barrier.

## Tech stack

| Layer | Tech |
|---|---|
| Frontend | React + Tailwind CSS |
| Backend API | Python (FastAPI) |
| Intelligence layer | scikit-learn eligibility model + Google Gemini API (voice / vernacular) |
| Data & hosting | Firebase (Firestore + Auth), Google Cloud Run |

## Repo structure

```
vishwasfund/
├── frontend/    # React + Tailwind web app
├── backend/     # FastAPI service, REST endpoints
├── ml/          # eligibility scoring model + training data
└── docs/        # architecture notes, data flow diagram
```

## Getting started

### Backend
```bash
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### ML model
```bash
cd ml
pip install -r requirements.txt
python train_eligibility_model.py
```

## Team

- Ekta Gupta — candyekta01@gmail.com
- Niharika Aggarwal — niharikaaggarwal53@gmail.com

## License

MIT — see [LICENSE](LICENSE).
