# ==========================================================
# FILE: explain_chain.py
# ----------------------------------------------------------
# PURPOSE:
# Connect prompt + model into a reusable chain.
#
# WHY THIS EXISTS:
# The prompt knows HOW to ask.
# The model knows HOW to generate.
#
# The chain connects both pieces.
#
# RESPONSIBILITIES:
# - Receive a topic
# - Build the prompt
# - Run the model
# - Return the response
#
# THIS FILE DOES NOT:
# - Route requests
# - Create UI
# - Expose APIs
# ==========================================================

from src.prompts.explain_prompt import explain_prompt
from src.models.model_loader import tokenizer, model


def explain_chain(topic: str) -> str:
    """
    Executes:
    Topic -> Prompt -> Model -> Response
    """

    # Build prompt
    prompt_text = explain_prompt.format(
        topic=topic
    )

    # Convert text to tokens
    inputs = tokenizer(
        prompt_text,
        return_tensors="pt"
    )

    # Generate response
    outputs = model.generate(
        **inputs,
        max_new_tokens=128
    )

    # Convert tokens back to text
    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response


if __name__ == "__main__":

    result = explain_chain(
        "machine learning"
    )

    print(result)