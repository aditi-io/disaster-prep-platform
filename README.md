\# Disaster-Preparedness Training Platform



Interactive web-based platform for training emergency responders in disaster response scenarios.



\## Features



\- 5 disaster scenarios (Earthquake, Flood, Fire, Chemical Spill, Power Outage)

\- Role-based access control (Responder, Trainer, Admin)

\- Real-time decision evaluation with instant feedback

\- Full-stack REST API architecture



\## Tech Stack



\- \*\*Backend:\*\* FastAPI (Python), REST API

\- \*\*Frontend:\*\* React, Axios

\- \*\*Deployment:\*\* Render (backend), Netlify (frontend)



\## Live Demo



\- Frontend: https://\[your-netlify-url].netlify.app

\- Backend API: https://disaster-prep-api.onrender.com



\## Local Setup



```bash

\# Backend

cd backend

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python main.py



\# Frontend (new terminal)

cd frontend

npm install

npm start

```



\## API Endpoints



\- `GET /scenarios` - Get all disaster scenarios

\- `GET /scenarios/{id}` - Get specific scenario  

\- `POST /simulate` - Evaluate user decision

\- `GET /health` - Health check



\## Deployment



\- Backend deployed on Render

\- Frontend deployed on Netlify

\- Both services communicate via REST API



\## Author



Aditi Maharor | B.Tech CSE 2028 | BIT Mesra

