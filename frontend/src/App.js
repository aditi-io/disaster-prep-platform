import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

const API_URL = 'http://localhost:8000';

function App() {
  const [scenarios, setScenarios] = useState([]);
  const [selectedScenario, setSelectedScenario] = useState(null);
  const [userRole, setUserRole] = useState('responder');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchScenarios();
  }, []);

  const fetchScenarios = async () => {
    try {
      const response = await axios.get(`${API_URL}/scenarios`);
      setScenarios(response.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching scenarios:', error);
      setLoading(false);
    }
  };

  const handleScenarioSelect = (scenario) => {
    setSelectedScenario(scenario);
    setResult(null);
  };

  const handleDecision = async (decision) => {
    try {
      const response = await axios.post(`${API_URL}/simulate`, {
        scenario_id: selectedScenario.id,
        user_choice: decision,
        user_role: userRole
      });
      setResult(response.data);
    } catch (error) {
      console.error('Error submitting decision:', error);
      alert('Error submitting decision: ' + error.message);
    }
  };

  if (loading) return <div className="container"><p>Loading scenarios...</p></div>;

  return (
    <div className="container">
      <h1>🚨 Disaster Preparedness Training Platform</h1>
      
      <div className="role-selector">
        <label>Select Your Role: </label>
        <select value={userRole} onChange={(e) => setUserRole(e.target.value)}>
          <option value="responder">Emergency Responder</option>
          <option value="trainer">Trainer</option>
          <option value="admin">Administrator</option>
        </select>
      </div>

      {!selectedScenario ? (
        <div className="scenarios-grid">
          {scenarios.map(scenario => (
            <div key={scenario.id} className="scenario-card">
              <h3>{scenario.name}</h3>
              <p className="description">{scenario.description}</p>
              <p className="severity">Severity: {scenario.severity}/5</p>
              <p className="category">{scenario.category}</p>
              <button onClick={() => handleScenarioSelect(scenario)}>
                Start Simulation
              </button>
            </div>
          ))}
        </div>
      ) : (
        <div className="simulation">
          <h2>{selectedScenario.name}</h2>
          <p className="scenario-description">{selectedScenario.description}</p>

          {!result ? (
            <div className="decision-options">
              <p className="decision-prompt">What's your decision?</p>
              <button className="decision-btn" onClick={() => handleDecision('evacuate_immediately')}>
                Evacuate Immediately
              </button>
              <button className="decision-btn" onClick={() => handleDecision('shelter_in_place')}>
                Shelter in Place
              </button>
              <button className="decision-btn" onClick={() => handleDecision('activate_evacuation')}>
                Activate Evacuation Protocol
              </button>
              <button className="decision-btn" onClick={() => handleDecision('containment_first')}>
                Containment First
              </button>
              <button className="decision-btn" onClick={() => handleDecision('activate_emergency_protocol')}>
                Activate Emergency Protocol
              </button>
              <button className="decision-btn" onClick={() => handleDecision('immediate_evacuation')}>
                Immediate Evacuation
              </button>
              <button className="decision-btn" onClick={() => handleDecision('wait_for_confirmation')}>
                Wait for Confirmation
              </button>
            </div>
          ) : (
            <div className="result">
              <h3 className={result.correct ? 'correct' : 'incorrect'}>
                {result.correct ? '✅ Correct!' : '❌ Incorrect'}
              </h3>
              <p><strong>Outcome:</strong> {result.outcome}</p>
              <p><strong>Score:</strong> {result.score}/100</p>
              <p><strong>Feedback:</strong> {result.feedback}</p>
              <button className="back-btn" onClick={() => {
                setSelectedScenario(null);
                setResult(null);
              }}>
                Back to Scenarios
              </button>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default App;