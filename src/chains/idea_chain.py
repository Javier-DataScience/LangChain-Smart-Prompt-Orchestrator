# ==========================================================
# FILE: idea_chain.py
# ----------------------------------------------------------
# PURPOSE:
# Connect idea prompt + model.
#
# RESPONSIBILITIES:
# - Receive topic
# - Build idea-generation prompt
# - Run model inference
# - Return generated ideas
# ==========================================================

from src.prompts.idea_prompt import idea_prompt
from src.models.model_loader import tokenizer, model
from src.config.settings import MAX_NEW_TOKENS


def idea_chain(topic: str) -> str:

    # Build prompt
    prompt_text = idea_prompt.format(
        topic=topic
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

    result = idea_chain(
        "fitness"
    )

    print(result)