# ==========================================================
# FILE: idea_prompt.py
# ----------------------------------------------------------
# PURPOSE:
# Store the prompt used for idea generation.
#
# WHY THIS EXISTS:
# Idea generation is different from explanation
# and summarization.
#
# RESPONSIBILITIES:
# - Define PromptTemplate
# - Expose idea_prompt object
#
# THIS FILE DOES NOT:
# - Load models
# - Run inference
# - Route requests
# ==========================================================

from langchain_core.prompts import PromptTemplate


idea_prompt = PromptTemplate.from_template(
    """
You are a creative startup advisor.

Generate 3 startup ideas about:

{topic}
"""
)