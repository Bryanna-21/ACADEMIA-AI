from fastapi import APIRouter
from pydantic import BaseModel
from llm_router import LLMRouter

router = APIRouter(prefix="/lesson", tags=["lesson-planner"])
llm = LLMRouter()

class LessonRequest(BaseModel):
    topic: str
    duration: int = 60
    persona: str = "standard"  # strict, fun, socratic, etc.

@router.post("/plan")
async def generate_lesson_plan(req: LessonRequest):
    prompt = f"Create a detailed {req.duration}-minute lesson plan on {req.topic} using a {req.persona} teaching persona."
    plan = await llm.query(prompt)
    return {"lesson_plan": plan, "persona": req.persona}
