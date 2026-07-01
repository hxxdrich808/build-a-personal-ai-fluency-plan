from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .agent import generate_fluency_plan

app = FastAPI(title="AI Fluency Plan Generator")

class PlanRequest(BaseModel):
    user_input: str

@app.post("/api/plan")
async def create_plan(request: PlanRequest):
    """
    Generate a personalized AI fluency plan based on the user's input.
    The request should contain a JSON body with a 'user_input' field
    describing the user's goals or context.
    """
    try:
        plan_text = generate_fluency_plan(request.user_input)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"plan": plan_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
