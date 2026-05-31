# ==========================================================
# FILE: summarize_chain.py
# ----------------------------------------------------------
# PURPOSE:
# Connect summarize prompt + model.
#
# RESPONSIBILITIES:
# - Receive text
# - Build summary prompt
# - Run model inference
# - Return summary
# ==========================================================

from src.prompts.summarize_prompt import summarize_prompt
from src.models.model_loader import tokenizer, model
from src.config.settings import MAX_NEW_TOKENS


def summarize_chain(text: str) -> str:

    # Build prompt
    prompt_text = summarize_prompt.format(
        text=text
    )

    # Tokenize
    inputs = tokenizer(
        prompt_text,
        return_tensors="pt"
    )

    # Generate
    outputs = model.generate(
        **inputs,
        max_new_tokens=MAX_NEW_TOKENS
    )

    # Decode
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