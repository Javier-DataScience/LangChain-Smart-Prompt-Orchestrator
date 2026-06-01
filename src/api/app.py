# ==========================================================
# FILE: app.py
# ----------------------------------------------------------
# PURPOSE:
# FastAPI entry point for LangChain Smart Prompt Orchestrator
#
# WHY THIS EXISTS:
# Exposes ML chains (explain, summarize, ideas) via HTTP API
# and provides a unified routing endpoint for the UI.
#
# ARCHITECTURE:
#
# Streamlit → FastAPI → Router → Chains → Model
# ==========================================================

from fastapi import FastAPI
from pydantic import BaseModel

from src.routers.rule_router import route_request

# ==========================================================
# REQUEST SCHEMA
# ==========================================================

class PromptRequest(BaseModel):
    text: str


# ==========================================================
# CREATE FASTAPI APP
# ==========================================================

app = FastAPI(
    title="LangChain Smart Prompt Orchestrator",
    description="Educational LLM orchestration project",
    version="1.0.0"
)


# ==========================================================
# HEALTH CHECK
# ==========================================================

@app.get("/")
def root():
    return {
        "message": "API is running successfully"
    }


# ==========================================================
# MAIN ROUTE (USED BY STREAMLIT UI)
# ==========================================================

@app.post("/route")
def route_endpoint(request: PromptRequest):
    """
    Receives user input and routes it to the correct chain
    using the smart router.
    """

    result = route_request(request.text)

    return {
        "response": result
    }