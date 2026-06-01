# ==========================================================
# FILE: explain_prompt.py
# ----------------------------------------------------------
# PURPOSE:
# Defines the prompt template used to generate explanations
# for technical topics in a simple and beginner-friendly way.
#
# WHY THIS EXISTS:
# This module standardizes how the model explains concepts
# to ensure clarity, consistency, and simplicity.
#
# DESIGN PRINCIPLE:
# - Keep prompts simple (important for small models like FLAN-T5-base)
# - Avoid over-structuring
# - Prevent instruction leakage into outputs
# ==========================================================

from langchain_core.prompts import PromptTemplate


explain_prompt = PromptTemplate.from_template(
"""
You are a helpful teacher.

Explain the topic in a clear and simple way for a beginner.

Rules:
- Use simple language
- Be correct and easy to understand
- Keep the explanation short but complete
- Do not repeat these instructions in your answer

Topic: {topic}

Explanation:
"""
)