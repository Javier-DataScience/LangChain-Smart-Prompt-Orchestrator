# ==========================================================
# FILE: app.py
# ----------------------------------------------------------
# PURPOSE:
# FastAPI application entry point.
#
# WHY THIS EXISTS:
# Expose our AI system through HTTP endpoints.
#
# ARCHITECTURE:
#
# Client
#    ↓
# FastAPI
#    ↓
# Endpoint
#    ↓
# Chain
#    ↓
# Prompt
#    ↓
# Model
#
# ==========================================================

from fastapi import FastAPI

from src.api.schemas import (
    ExplainRequest,
    SummarizeRequest,
    IdeaRequest
)

from src.chains.explain_chain import explain_chain
from src.chains.summarize_chain import summarize_chain
from src.chains.idea_chain import idea_chain


# ==========================================================
# CREATE APPLICATION
# ==========================================================

app = FastAPI(
    title="LangChain Smart Prompt Orchestrator",
    description="Educational LLM orchestration project",
    version="1.0.0"
)


# ==========================================================
# HEALTH CHECK ENDPOINT
# ----------------------------------------------------------
# Used to verify the API is running.
# ==========================================================

@app.get("/")
def root():

    return {
        "message": "API is running successfully"
    }


# ==========================================================
# EXPLAIN ENDPOINT
# ----------------------------------------------------------
# Example Request:
#
# {
#     "topic": "machine learning"
# }
# ==========================================================

@app.post("/explain")
def explain(request: ExplainRequest):

    response = explain_chain(
        request.topic
    )

    return {
        "response": response
    }


# ==========================================================
# SUMMARIZE ENDPOINT
# ----------------------------------------------------------
# Example Request:
#
# {
#     "text": "Artificial intelligence is transforming industries."
# }
# ==========================================================

@app.post("/summarize")
def summarize(request: SummarizeRequest):

    response = summarize_chain(
        request.text
    )

    return {
        "response": response
    }


# ==========================================================
# IDEAS ENDPOINT
# ----------------------------------------------------------
# Example Request:
#
# {
#     "topic": "fitness"
# }
# ==========================================================

@app.post("/ideas")
def ideas(request: IdeaRequest):

    response = idea_chain(
        request.topic
    )

    return {
        "response": response
    }