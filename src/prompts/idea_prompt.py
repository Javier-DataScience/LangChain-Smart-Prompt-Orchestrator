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
You are a startup advisor.

Generate 3 REAL startup ideas.

RULES:
- Each idea must be practical
- Each idea must include what problem it solves
- Avoid random or single words

TOPIC:
{topic}

FORMAT:
1.
2.
3.
"""
)