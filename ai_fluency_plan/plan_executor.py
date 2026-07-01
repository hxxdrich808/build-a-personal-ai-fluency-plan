"""
Plan Executor Script

This script simulates the execution of the AI fluency development plan.
It prints scheduled tasks and checks completion status based on a simple
JSON state file (`plan_state.json`). The script can be extended to integrate
with LangChain or other automation tools.
"""

import json
import os
from datetime import datetime, timedelta

STATE_FILE = "ai_fluency_plan/plan_state.json"

# Define the plan milestones
PLAN = [
    {"week": 1, "task": "Collect dataset and perform initial exploration", "completed": False},
    {"week": 2, "task": "Clean data and handle missing values", "completed": False},
    {"week": 3, "task": "Build linear regression model", "completed": False},
    {"week": 4, "task": "Evaluate model performance", "completed": False},
    {"week": 5, "task": "Research bias mitigation techniques", "completed": False},
    {"week": 6, "task": "Write bias mitigation essay", "completed": False},
    {"week": 7, "task": "Design rule‑based chatbot using LangChain", "completed": False},
    {"week": 8, "task": "Deploy chatbot prototype", "completed": False},
    {"week": 9, "task": "Test chatbot for hallucinations", "completed": False},
    {"week": 10, "task": "Document evaluation findings", "completed": False},
    {"week": 11, "task": "Create presentation slides", "completed": False},
    {"week": 12, "task": "Deliver final report and reflection log", "completed": False},
]

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)

def simulate_execution():
    state = load_state()
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())  # Monday of current week

    print(f"Simulation started on {today} (Week starting: {week_start})\n")
    for idx, milestone in enumerate(PLAN):
        scheduled_week = week_start + timedelta(weeks=idx)
        status = state.get(str(idx), False)
        print(f"[Week {idx+1}] ({scheduled_week}) - {milestone['task']}")
        if status:
            print("   ✅ Completed")
        else:
            print("   ❌ Pending")

    # Prompt user to mark a milestone as completed
    try:
        choice = int(input("\nEnter the week number you have just completed (0 to skip): "))
        if 1 <= choice <= len(PLAN):
            state[str(choice-1)] = True
            save_state(state)
            print(f"Week {choice} marked as completed.")
        else:
            print("No changes made.")
    except ValueError:
        print("Invalid input. Exiting without changes.")

if __name__ == "__main__":
    simulate_execution()
