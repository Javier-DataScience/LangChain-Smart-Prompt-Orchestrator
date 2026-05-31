# ==========================================================
# FILE: summarize_prompt.py
# ----------------------------------------------------------
# PURPOSE:
# Store the prompt used for summarization tasks.
#
# WHY THIS EXISTS:
# Different tasks require different prompts.
#
# An explanation prompt teaches.
# A summarization prompt compresses information.
#
# RESPONSIBILITIES:
# - Define PromptTemplate
# - Expose summarize_prompt object
#
# THIS FILE DOES NOT:
# - Load models
# - Generate responses
# - Route requests
# ==========================================================

from langchain_core.prompts import PromptTemplate


summarize_prompt = PromptTemplate.from_template(
    """
You are a helpful assistant.

Summarize the following text in 2-3 short sentences.

Text:
{text}
"""
)