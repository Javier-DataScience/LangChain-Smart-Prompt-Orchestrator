# ==========================================================
# FILE: summarize_prompt.py
# ----------------------------------------------------------
# PURPOSE:
# Force real compression behavior in small LLMs
#
# WHY THIS EXISTS:
# FLAN-T5-base tends to paraphrase instead of summarizing
#
# GOAL:
# Make the model REMOVE details, not rewrite them
# ==========================================================

from langchain_core.prompts import PromptTemplate


summarize_prompt = PromptTemplate.from_template(
"""
You are a text compression system.

Your job is to reduce the text to ONLY its most important idea.

IMPORTANT RULES:
- Remove all extra details
- Do NOT repeat sentences from the original text
- Do NOT paraphrase line by line
- Keep ONLY the core message
- Output must be shorter than the input

OUTPUT FORMAT:
A short paragraph with only the main idea.

TEXT:
{text}

COMPRESSED SUMMARY:
"""
)