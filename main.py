
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/status")
async def status():
    return {"status": "active", "ai_engine": "Gemini 1.5 Pro", "maintenance": "auto"}
