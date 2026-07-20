from fastapi import FastAPI
from dotenv import load_dotenv
from .llm_router import LLMRouter
from .routers.admin import router as admin_router
from .routers.classes import router as classes_router
from .routers.voice import router as voice_router
from .routers.payment import router as payment_router
from .routers.diagnostics import router as diagnostics_router
from .routers.websocket import router as ws_router

load_dotenv()

app = FastAPI(title="Academia AI")

app.include_router(admin_router)
app.include_router(classes_router)
app.include_router(voice_router)
app.include_router(payment_router)
app.include_router(diagnostics_router)
app.include_router(ws_router)

llm = LLMRouter()

@app.get("/")
async def root():
    return {"message": "Academia AI Backend is live. How may I assist you today, Sir?"}

@app.get("/test-llm")
async def test_llm(prompt: str = "Hello"):
    return await llm.query(prompt)
