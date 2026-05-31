# ==========================================================
# FILE: summarize_chain.py
# ----------------------------------------------------------
# PURPOSE:
# Connect summarize prompt + model.
#
# FLOW:
# Text
#   ↓
# PromptTemplate
#   ↓
# HuggingFace Model
#   ↓
# Response
# ==========================================================

from src.prompts.summarize_prompt import summarize_prompt
from src.models.model_loader import tokenizer, model


def summarize_chain(text: str) -> str:

    prompt_text = summarize_prompt.format(
        text=text
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

    result = summarize_chain(
        "Artificial intelligence is transforming industries."
    )

    print(result)