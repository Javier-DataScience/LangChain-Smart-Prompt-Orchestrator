# ==========================================================
# FILE: explain_prompt.py
# ----------------------------------------------------------
# PURPOSE:
# Store the explanation prompt used by the application.
#
# WHY THIS EXISTS:
# In the notebook, prompts were defined directly inside
# cells.
#
# In a real project, prompts are separated from chains,
# routers, and model code.
#
# RESPONSIBILITIES:
# - Define PromptTemplate
# - Expose prompt object
#
# THIS FILE DOES NOT:
# - Load models
# - Run inference
# - Route requests
# ==========================================================

from langchain_core.prompts import PromptTemplate


explain_prompt = PromptTemplate.from_template(
    """
You are a helpful teacher.

Explain the topic in a simple way for a beginner.

Topic:
{topic}
"""
)