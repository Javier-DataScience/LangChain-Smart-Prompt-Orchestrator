# ==========================================================
# FILE: rule_router.py
# ----------------------------------------------------------
# PURPOSE:
# Smart routing system for selecting the correct LLM chain
#
# WHY THIS EXISTS:
# Instead of fragile keyword rules, we use structured intent
# classification logic to route user requests.
#
# ARCHITECTURE:
#
# User Input
#     ↓
# Router (this file)
#     ↓
# Explain / Summarize / Ideas Chain
#     ↓
# Model
# ==========================================================


# ==========================================================
# IMPORT CHAINS
# ==========================================================

from src.chains.explain_chain import explain_chain
from src.chains.summarize_chain import summarize_chain
from src.chains.idea_chain import idea_chain


# ==========================================================
# INTENT DETECTION FUNCTION
# ==========================================================

def detect_intent(text: str) -> str:
    """
    Simple but robust intent classification
    """

    text_lower = text.lower()

    # ------------------------------------------------------
    # EXPLAIN INTENT
    # ------------------------------------------------------
    if any(word in text_lower for word in ["explain", "what is", "define"]):
        return "explain"

    # ------------------------------------------------------
    # SUMMARIZE INTENT
    # ------------------------------------------------------
    if any(word in text_lower for word in ["summarize", "summary", "resume"]):
        return "summarize"

    # ------------------------------------------------------
    # IDEA INTENT
    # ------------------------------------------------------
    if any(word in text_lower for word in ["idea", "ideas", "startup", "business"]):
        return "ideas"

    # ------------------------------------------------------
    # DEFAULT FALLBACK
    # ------------------------------------------------------
    return "explain"


# ==========================================================
# MAIN ROUTER FUNCTION
# ==========================================================

def route_request(user_input: str) -> str:
    """
    Routes input to correct LLM chain
    """

    intent = detect_intent(user_input)

    # ------------------------------------------------------
    # ROUTING LOGIC
    # ------------------------------------------------------

    if intent == "explain":
        return explain_chain(user_input)

    elif intent == "summarize":
        return summarize_chain(user_input)

    elif intent == "ideas":
        return idea_chain(user_input)

    # fallback safety
    return explain_chain(user_input)