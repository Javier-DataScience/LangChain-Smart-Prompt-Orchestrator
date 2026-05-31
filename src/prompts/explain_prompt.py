# ==========================================================
# FILE: explain_prompt.py
# ----------------------------------------------------------
# PURPOSE:
# High-quality instruction prompt for explanation tasks.
#
# WHY:
# Small models need extremely explicit structure.
# ==========================================================

from langchain_core.prompts import PromptTemplate


explain_prompt = PromptTemplate.from_template(
    """
You are an expert teacher.

Explain the topic in a very simple and clear way.

RULES:
- Use exactly 2 short sentences
- First sentence: definition
- Second sentence: real-world example
- Do NOT repeat the topic word multiple times

TOPIC:
{topic}
"""
)