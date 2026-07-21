from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

class Login(BaseModel):
    username: str
    password: str

@router.post("/login")
async def login(credentials: Login):
    # Placeholder - add real auth later (JWT)
    if credentials.username == "admin":
        return {"token": "super_secret_token", "role": "superadmin"}
    raise HTTPException(401, "Invalid credentials")
