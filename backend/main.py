from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from llm_router import LLMRouter

# Routers
from routers.admin import router as admin_router
from routers.classes import router as classes_router
from routers.voice import router as voice_router
from routers.payment import router as payment_router
from routers.diagnostics import router as diagnostics_router
from routers.websocket import router as ws_router
from routers.assignments import router as assignments_router
from routers.auth import router as auth_router
from routers.webrtc import router as webrtc_router   # New

load_dotenv()

app = FastAPI(title="Academia AI", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin_router)
app.include_router(classes_router)
app.include_router(voice_router)
app.include_router(payment_router)
app.include_router(diagnostics_router)
app.include_router(ws_router)
app.include_router(assignments_router)
app.include_router(auth_router)
app.include_router(webrtc_router)   # Added for screen sharing

llm = LLMRouter()

@app.get("/")
async def root():
    return {"message": "Academia AI is operational. At your service, Sir."}

@app.get("/health")
async def health():
    return {"status": "healthy"}
