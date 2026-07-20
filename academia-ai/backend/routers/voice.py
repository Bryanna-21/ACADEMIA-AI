from fastapi import APIRouter, UploadFile, File
from ..voice_cloning import capture_voice_sample

router = APIRouter(prefix="/voice", tags=["voice"])

@router.post("/setup")
async def setup_voice(audio: UploadFile = File(...), text: str = "This is a test for voice cloning"):
    result = await capture_voice_sample(audio, text)
    return result
