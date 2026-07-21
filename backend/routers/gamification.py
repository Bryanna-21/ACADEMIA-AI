from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/gamification", tags=["gamification"])

class Progress(BaseModel):
    student_id: int
    points: int = 0

@router.post("/award")
async def award_points(progress: Progress):
    return {
        "student_id": progress.student_id,
        "new_points": progress.points + 50,
        "badge": "Knowledge Seeker",
        "message": "Congratulations! New badge unlocked."
    }
