# ==========================================================
# FILE: rule_router.py
# ----------------------------------------------------------
# PURPOSE:
# Route user requests to the correct chain.
#
# WHY THIS EXISTS:
# Instead of calling chains directly,
# users interact with a single entry point.
#
# FLOW:
#
# User Request
#       ↓
# Router
#       ↓
# Select Chain
#       ↓
# Return Response
#
# ==========================================================

from src.chains.explain_chain import explain_chain
from src.chains.summarize_chain import summarize_chain
from src.chains.idea_chain import idea_chain


def route_request(user_input: str) -> str:

    request = user_input.lower()

    if "explain" in request:
        return explain_chain(user_input)

    elif "summarize" in request:
        return summarize_chain(user_input)

    elif "idea" in request:
        return idea_chain(user_input)

    else:
        return "No valid chain found."


if __name__ == "__main__":

    tests = [
        "Explain machine learning",
        "Summarize AI is transforming industries",
        "Give me startup ideas about fitness"
    ]

    for t in tests:

        print("\nINPUT:", t)
        print("OUTPUT:", route_request(t))