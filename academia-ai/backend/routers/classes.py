from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/classes", tags=["classes"])

class ClassCreate(BaseModel):
    title: str
    description: str

@router.post("/")
async def create_class(class_data: ClassCreate):
    # TODO: Save to DB + generate invite link
    return {"class_id": 101, "invite_link": "https://academia-ai.com/join/abc123", "message": "Class created. Link ready for sharing."}

@router.get("/invite/{class_id}")
async def get_invite_link(class_id: int):
    return {"invite_link": f"https://academia-ai.com/join/{class_id}"}
