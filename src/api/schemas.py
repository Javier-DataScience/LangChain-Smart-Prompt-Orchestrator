# ==========================================================
# FILE: schemas.py
# ----------------------------------------------------------
# PURPOSE:
# Define request schemas for FastAPI endpoints.
#
# WHY:
# FastAPI uses Pydantic models to validate
# incoming requests automatically.
#
# RESPONSIBILITIES:
# - Validate incoming API requests
# - Define expected fields
# - Provide automatic Swagger documentation
#
# THIS FILE DOES NOT:
# - Run models
# - Execute chains
# - Route requests
# ==========================================================

from pydantic import BaseModel


# ==========================================================
# EXPLAIN REQUEST
# ----------------------------------------------------------
# Example:
#
# {
#     "topic": "machine learning"
# }
# ==========================================================

class ExplainRequest(BaseModel):
    topic: str


# ==========================================================
# SUMMARIZE REQUEST
# ----------------------------------------------------------
# Example:
#
# {
#     "text": "Artificial intelligence is transforming industries."
# }
# ==========================================================

class SummarizeRequest(BaseModel):
    text: str


# ==========================================================
# IDEA REQUEST
# ----------------------------------------------------------
# Example:
#
# {
#     "topic": "fitness"
# }
# ==========================================================

class IdeaRequest(BaseModel):
    topic: str