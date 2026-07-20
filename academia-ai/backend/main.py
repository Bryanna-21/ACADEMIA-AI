from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Academia AI")

@app.get("/")
async def root():
    return {"message": "Academia AI Backend is running. Sir."}

@app.get("/health")
async def health():
    return {"status": "healthy"}
