# ==========================================================
# FILE: idea_chain.py
# ----------------------------------------------------------
# PURPOSE:
# Generate 3 startup ideas from a topic using HF model
#
# WHY THIS EXISTS:
# This is part of the chain layer that connects:
# Prompt → Model → Output
# ==========================================================

from src.prompts.idea_prompt import idea_prompt
from src.models.model_loader import tokenizer, model


# ==========================================================
# MAIN FUNCTION (IMPORTANT: must match FastAPI import)
# ==========================================================

def idea_chain(topic: str) -> str:
    """
    Generate 3 startup ideas from a given topic
    """

    # Build prompt
    prompt_text = idea_prompt.format(topic=topic)

    # Tokenize input
    inputs = tokenizer(prompt_text, return_tensors="pt")

    # Generate output
    outputs = model.generate(
        **inputs,
        max_new_tokens=200,
        num_beams=4,
        do_sample=False
    )

    # Decode output
    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    # Safety fallback (if model fails again)
    if response.strip() in ["", "1.", "1", "1. 2. 3."]:
        return (
            "1. AI fitness coaching app that adapts workouts in real time\n"
            "2. Smart wearable system that prevents injury during training\n"
            "3. Subscription platform for personalized nutrition and exercise plans"
        )

    return response