from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/engagement", tags=["engagement"])

class EngagementData(BaseModel):
    student_id: int
    emotion: str = "neutral"  # happy, confused, bored

@router.post("/detect")
async def detect_engagement(data: EngagementData):
    suggestions = {
        "bored": "Introduce interactive quiz",
        "confused": "Explain concept with simpler analogy"
    }
    return {
        "student_id": data.student_id,
        "detected_emotion": data.emotion,
        "suggestion": suggestions.get(data.emotion, "Continue as planned")
    }
