# ==========================================================
# FILE: idea_chain.py
# ----------------------------------------------------------
# PURPOSE:
# Connect idea prompt + model.
#
# FLOW:
# Topic
#   ↓
# PromptTemplate
#   ↓
# HuggingFace Model
#   ↓
# Response
# ==========================================================

from src.prompts.idea_prompt import idea_prompt
from src.models.model_loader import tokenizer, model


def idea_chain(topic: str) -> str:

    prompt_text = idea_prompt.format(
        topic=topic
    )

    inputs = tokenizer(
        prompt_text,
        return_tensors="pt"
    )

    outputs = model.generate(
        **inputs,
        max_new_tokens=128
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response


if __name__ == "__main__":

    result = idea_chain(
        "fitness"
    )

    print(result)