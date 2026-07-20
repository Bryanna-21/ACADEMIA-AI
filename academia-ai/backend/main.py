from fastapi import FastAPI
from dotenv import load_dotenv
from .llm_router import LLMRouter
from .routers.admin import router as admin_router

load_dotenv()

app = FastAPI(title="Academia AI")

app.include_router(admin_router)

llm = LLMRouter()

@app.get("/")
async def root():
    return {"message": "Academia AI Backend running. Sir."}

@app.get("/test-llm")
async def test_llm(prompt: str = "Hello"):
    return await llm.query(prompt)
