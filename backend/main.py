from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Disaster Prep Platform", version="1.0")

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ========== DATA MODELS ==========
class Scenario(BaseModel):
    id: int
    name: str
    description: str
    category: str
    severity: int

class UserResponse(BaseModel):
    scenario_id: int
    user_choice: str
    user_role: str

class SimulationResult(BaseModel):
    correct: bool
    correct_action: str
    outcome: str
    score: int
    feedback: str

# ========== SCENARIOS DATA ==========
SCENARIOS = [
    {
        "id": 1,
        "name": "Earthquake Response",
        "description": "Building collapsed, 50 people trapped. Power out. What do you do?",
        "category": "Natural Disaster",
        "severity": 5,
        "decisions": {
            "evacuate_immediately": {
                "correct": True,
                "outcome": "Emergency teams mobilized, rescue operations begin successfully",
                "score": 100
            },
            "shelter_in_place": {
                "correct": False,
                "outcome": "Delays reduce survival chances",
                "score": 30
            },
            "activate_evacuation": {
                "correct": False,
                "outcome": "Delays reduce survival chances",
                "score": 30
            },
            "containment_first": {
                "correct": False,
                "outcome": "Wrong priority in earthquake scenario",
                "score": 20
            },
            "activate_emergency_protocol": {
                "correct": False,
                "outcome": "Wrong priority in earthquake scenario",
                "score": 20
            },
            "immediate_evacuation": {
                "correct": True,
                "outcome": "Emergency teams mobilized, rescue operations begin successfully",
                "score": 100
            },
            "wait_for_confirmation": {
                "correct": False,
                "outcome": "Critical time lost",
                "score": 20
            }
        }
    },
    {
        "id": 2,
        "name": "Flood Management",
        "description": "River overflow detected, 2 hours to peak flood. How do you respond?",
        "category": "Natural Disaster",
        "severity": 4,
        "decisions": {
            "evacuate_immediately": {
                "correct": True,
                "outcome": "All residents evacuated safely before peak flood",
                "score": 100
            },
            "shelter_in_place": {
                "correct": False,
                "outcome": "Infrastructure damage, people trapped",
                "score": 40
            },
            "activate_evacuation": {
                "correct": True,
                "outcome": "All residents evacuated safely before peak flood",
                "score": 100
            },
            "containment_first": {
                "correct": False,
                "outcome": "Evacuation delayed, lives at risk",
                "score": 35
            },
            "activate_emergency_protocol": {
                "correct": False,
                "outcome": "Evacuation delayed, lives at risk",
                "score": 35
            },
            "immediate_evacuation": {
                "correct": True,
                "outcome": "All residents evacuated safely before peak flood",
                "score": 100
            },
            "wait_for_confirmation": {
                "correct": False,
                "outcome": "Confirmation delays evacuation, water rises",
                "score": 30
            }
        }
    },
    {
        "id": 3,
        "name": "Fire Emergency",
        "description": "Office building fire detected. 200+ people inside. What's your first action?",
        "category": "Man-made",
        "severity": 4,
        "decisions": {
            "evacuate_immediately": {
                "correct": True,
                "outcome": "Orderly evacuation complete, 0 casualties",
                "score": 100
            },
            "shelter_in_place": {
                "correct": False,
                "outcome": "Fire spreads faster, increased casualties",
                "score": 35
            },
            "activate_evacuation": {
                "correct": True,
                "outcome": "Orderly evacuation complete, 0 casualties",
                "score": 100
            },
            "containment_first": {
                "correct": False,
                "outcome": "Evacuation delayed, casualties increase",
                "score": 30
            },
            "activate_emergency_protocol": {
                "correct": False,
                "outcome": "Evacuation delayed, casualties increase",
                "score": 30
            },
            "immediate_evacuation": {
                "correct": True,
                "outcome": "Orderly evacuation complete, 0 casualties",
                "score": 100
            },
            "wait_for_confirmation": {
                "correct": False,
                "outcome": "Dangerous delay in evacuation",
                "score": 25
            }
        }
    },
    {
        "id": 4,
        "name": "Chemical Spill",
        "description": "Hazmat truck accident. Toxic fumes spreading. Priority?",
        "category": "Industrial",
        "severity": 5,
        "decisions": {
            "evacuate_immediately": {
                "correct": False,
                "outcome": "Spill spreads unchecked, environmental damage severe",
                "score": 50
            },
            "shelter_in_place": {
                "correct": False,
                "outcome": "Toxic exposure to residents",
                "score": 30
            },
            "activate_evacuation": {
                "correct": False,
                "outcome": "Spill spreads unchecked, environmental damage severe",
                "score": 50
            },
            "containment_first": {
                "correct": True,
                "outcome": "Spill contained, nearby area secured, minimal spread",
                "score": 100
            },
            "activate_emergency_protocol": {
                "correct": True,
                "outcome": "Spill contained, nearby area secured, minimal spread",
                "score": 100
            },
            "immediate_evacuation": {
                "correct": False,
                "outcome": "Spill spreads unchecked, environmental damage severe",
                "score": 50
            },
            "wait_for_confirmation": {
                "correct": False,
                "outcome": "Spill already spreading, confirmation delays response",
                "score": 25
            }
        }
    },
    {
        "id": 5,
        "name": "Power Grid Failure",
        "description": "City-wide power outage. Hospitals on backup. What's your move?",
        "category": "Infrastructure",
        "severity": 3,
        "decisions": {
            "evacuate_immediately": {
                "correct": False,
                "outcome": "Unnecessary evacuation causes chaos",
                "score": 25
            },
            "shelter_in_place": {
                "correct": False,
                "outcome": "Hospital backup power depletes, critical services at risk",
                "score": 25
            },
            "activate_evacuation": {
                "correct": False,
                "outcome": "Unnecessary evacuation causes chaos",
                "score": 25
            },
            "containment_first": {
                "correct": False,
                "outcome": "Not applicable to power outage",
                "score": 30
            },
            "activate_emergency_protocol": {
                "correct": True,
                "outcome": "Critical services maintained, grid restoration underway",
                "score": 100
            },
            "immediate_evacuation": {
                "correct": False,
                "outcome": "Unnecessary evacuation causes chaos",
                "score": 25
            },
            "wait_for_confirmation": {
                "correct": False,
                "outcome": "Hospital backup power depletes, critical services at risk",
                "score": 25
            }
        }
    }
]

# ========== ENDPOINTS ==========

@app.get("/")
async def root():
    return {
        "message": "Disaster Preparedness Training Platform API",
        "status": "healthy",
        "version": "1.0"
    }

@app.get("/scenarios", response_model=List[Scenario])
async def get_scenarios():
    """Get all disaster scenarios"""
    return [
        {
            "id": s["id"],
            "name": s["name"],
            "description": s["description"],
            "category": s["category"],
            "severity": s["severity"]
        }
        for s in SCENARIOS
    ]

@app.get("/scenarios/{scenario_id}", response_model=Scenario)
async def get_scenario(scenario_id: int):
    """Get specific scenario"""
    scenario = next((s for s in SCENARIOS if s["id"] == scenario_id), None)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")
    return {
        "id": scenario["id"],
        "name": scenario["name"],
        "description": scenario["description"],
        "category": scenario["category"],
        "severity": scenario["severity"]
    }

@app.post("/simulate", response_model=SimulationResult)
async def simulate(response: UserResponse):
    """Evaluate user's decision in a scenario"""
    scenario = next((s for s in SCENARIOS if s["id"] == response.scenario_id), None)
    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")
    
    decision = scenario["decisions"].get(response.user_choice)
    if not decision:
        raise HTTPException(status_code=400, detail=f"Invalid decision '{response.user_choice}' for this scenario")
    
    return SimulationResult(
        correct=decision["correct"],
        correct_action=response.user_choice,
        outcome=decision["outcome"],
        score=decision["score"],
        feedback="Excellent decision! Your response minimizes casualties and damage." if decision["correct"] else "Consider a different approach. This decision could have worse outcomes."
    )

@app.post("/role-based-access/{user_role}")
async def role_based_access(user_role: str):
    """Demonstrate role-based access control"""
    valid_roles = ["responder", "trainer", "admin"]
    if user_role not in valid_roles:
        raise HTTPException(status_code=403, detail="Invalid role")
    
    permissions = {
        "responder": ["view_scenarios", "submit_decisions"],
        "trainer": ["view_scenarios", "submit_decisions", "view_analytics"],
        "admin": ["manage_users", "manage_scenarios", "view_analytics", "generate_reports"]
    }
    
    return {
        "role": user_role,
        "permissions": permissions[user_role],
        "status": "access_granted"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "disaster-prep-platform",
        "version": "1.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)