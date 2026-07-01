import { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [milestones, setMilestones] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/milestones')
      .then((res) => res.json())
      .then(setMilestones);
  }, []);

  const toggleStatus = (id) => {
    const m = milestones.find((m) => m.id === id);
    const newStatus = m.status === 'completed' ? 'pending' : 'completed';
    fetch(`http://localhost:5000/api/milestones/${id}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ status: newStatus })
    })
      .then((res) => res.json())
      .then(() => {
        setMilestones(
          milestones.map((m) =>
            m.id === id ? { ...m, status: newStatus } : m
          )
        );
      });
  };

  return (
    <div className="App">
      <h1>AI Fluency Milestone Tracker</h1>
      <ul>
        {milestones.map((m) => (
          <li key={m.id}>
            <span style={{ textDecoration: m.status === 'completed' ? 'line-through' : 'none' }}>
              {m.title}
            </span>{' '}
            - Status:{' '}
            <strong>{m.status}</strong>{' '}
            <button onClick={() => toggleStatus(m.id)}>
              Mark as {m.status === 'completed' ? 'Pending' : 'Completed'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
