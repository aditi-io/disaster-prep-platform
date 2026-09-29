# Disaster-Preparedness Training Platform

A web app I built to simulate emergency response scenarios. Pick a disaster, make a decision, and see if it works out.

## Live Demo

Check it out here: https://disaster-preparedness-platform.netlify.app

(Backend: https://disaster-prep-platform-1.onrender.com if you want to test the API directly)

## What it does

- 5 different disaster scenarios (earthquake, flood, fire, chemical spill, power outage)
- Choose your role (responder, trainer, or admin - different people see different things)
- Pick a decision for each scenario
- Get instant feedback on whether you chose right or not
- See your score and what would've happened

## Built with

- FastAPI for the backend (Python)
- React for the frontend
- Render for hosting the backend
- Netlify for hosting the frontend

## Running locally

**Backend first:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # on Mac/Linux, or venv\Scripts\activate on Windows
pip install -r requirements.txt
python main.py
```

Then **frontend in a new terminal:**
```bash
cd frontend
npm install
npm start
```

Open http://localhost:3000 and you're good to go.

## How the API works

- `GET /scenarios` - pulls all 5 scenarios
- `GET /scenarios/{id}` - gets one scenario
- `POST /simulate` - you send your decision, it tells you if you were right
- `GET /health` - just checks if the server's up

## About me

Aditi Maharor - CS student at BIT Mesra, graduating 2028. CGPA 8.52.

GitHub: https://github.com/aditi-io
LinkedIn: https://linkedin.com/in/aditimaharor
