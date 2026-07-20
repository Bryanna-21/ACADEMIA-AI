from fastapi import APIRouter

router = APIRouter(prefix="/diagnostics", tags=["diagnostics"])

@router.get("/overview")
async def diagnostics_overview():
    return {
        "total_installs_tracked": 23,
        "active_sessions": 7,
        "api_usage": "Grok: 45%, OpenAI: 30%, Gemini: 25%",
        "issues": ["2 instances with voice cloning warnings"]
    }
