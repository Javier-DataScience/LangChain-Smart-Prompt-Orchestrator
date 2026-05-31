# ==========================================================
# FILE: settings.py
# ----------------------------------------------------------
# PURPOSE:
# Central place for application configuration.
#
# WHY:
# Avoid hardcoded values throughout the codebase.
#
# ==========================================================

# ----------------------------------------------------------
# HuggingFace Model Configuration
# ----------------------------------------------------------

MODEL_NAME = "google/flan-t5-small"

# ----------------------------------------------------------
# Generation Configuration
# ----------------------------------------------------------

MAX_NEW_TOKENS = 128