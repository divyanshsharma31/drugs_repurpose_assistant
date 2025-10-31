Team Name- Risk Raiders (078)
Team Members- Divyansh Sharma(Leader), Prashant Rana, Anant Agarwal, Harshit Kumawat

# Drug Discovery & Repurposing Assistant (EY PS#11)

AI-powered research agent that scans literature and clinical trials to surface drug repurposing opportunities. End-to-end MVP: FastAPI backend + React dashboard. Real APIs: PubMed, ClinicalTrials.gov, PubChem.

## Quick start

Backend
- python 3.9+
- pip install -r backend/requirements.txt
- python backend/main.py

Frontend
- Node 18+
- cd frontend && npm install && npm run dev

Open http://localhost:5173 (frontend) and ensure backend at http://localhost:8000

## Features
- Fetch abstracts from PubMed and trials from ClinicalTrials.gov
- Extract potential new indications
- Generate short summaries and confidence scoring
- Dashboard with search, result cards, and charts

## Endpoints
- GET /api/repurpose?drug=NAME
- GET /api/literature?drug=NAME
- GET /api/trials?drug=NAME
- GET /api/drug/{name}
- POST /api/analyze

## Notes
- Uses public APIs. No keys required.
- NLP kept lightweight for hackathon speed.
