from fastapi import APIRouter
from pydantic import BaseModel
from llm_router import LLMRouter

router = APIRouter(prefix="/assignments", tags=["assignments"])
llm = LLMRouter()

class AssignmentRequest(BaseModel):
    topic: str
    level: str = "intermediate"

@router.post("/generate")
async def generate_assignment(req: AssignmentRequest):
    prompt = f"Generate a detailed assignment on {req.topic} for {req.level} level students."
    response = await llm.query(prompt)
    return {"assignment": response, "message": "Assignment generated successfully."}
