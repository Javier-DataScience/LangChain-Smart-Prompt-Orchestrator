from langchain_core.prompts import PromptTemplate


summarize_prompt = PromptTemplate.from_template(
    """
You are a professional summarizer.

Summarize the text below.

RULES:
- 1 to 2 sentences only
- Keep meaning, remove repetition
- Do NOT copy the original sentence

TEXT:
{text}
"""
)