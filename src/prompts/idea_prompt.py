# ==========================================================
# FILE: idea_prompt.py
# ----------------------------------------------------------
# PURPOSE:
# Generates 3 simple startup ideas based on a given topic.
#
# WHY THIS EXISTS:
# Provides structured creativity generation for business ideas
# in a predictable and readable format.
#
# DESIGN PRINCIPLE:
# - Ensure creativity without over-constraining the model
# - Avoid empty outputs or instruction repetition
# - Keep output simple and stable for FLAN-T5-base
# ==========================================================

from langchain_core.prompts import PromptTemplate


idea_prompt = PromptTemplate.from_template(
"""
You are a creative startup advisor.

Generate 3 simple and practical startup ideas based on the topic.

Rules:
- Each idea must be one complete sentence
- Ideas must be realistic and useful
- Do not repeat instructions in your answer

Topic: {topic}

Ideas:
1.
2.
3.
"""
)