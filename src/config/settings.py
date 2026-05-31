# ==========================================================
# FILE: settings.py
# ----------------------------------------------------------
# PURPOSE:
# Central configuration for the entire system.
#
# WHY:
# Keeps model settings, generation parameters,
# and future environment variables in one place.
# ==========================================================

# ==========================================================
# MODEL CONFIGURATION
# ==========================================================

MODEL_NAME = "google/flan-t5-base"

# ==========================================================
# GENERATION CONFIGURATION
# ==========================================================

MAX_NEW_TOKENS = 128