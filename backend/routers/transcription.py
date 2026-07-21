from fastapi import APIRouter
from pydantic import BaseModel
from llm_router import LLMRouter

router = APIRouter(prefix="/transcription", tags=["transcription"])
llm = LLMRouter()

class TranscriptRequest(BaseModel):
    text: str
    class_id: int

@router.post("/summarize")
async def summarize_class(req: TranscriptRequest):
    prompt = f"Summarize this class transcript and highlight key points: {req.text[:2000]}"
    summary = await llm.query(prompt)
    return {"summary": summary, "key_points": ["Point 1", "Point 2"]}
