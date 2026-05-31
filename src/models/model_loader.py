# ==========================================================
# FILE: model_loader.py
# ----------------------------------------------------------
# PURPOSE:
# Load the HuggingFace model and tokenizer.
#
# WHY THIS EXISTS:
# We want a single place responsible for
# loading AI models.
#
# BENEFITS:
# - Avoid duplicate model loading
# - Centralize model initialization
# - Make model upgrades easier
#
# ARCHITECTURE:
#
# settings.py
#      ↓
# model_loader.py
#      ↓
# chains/
#
# ==========================================================

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from src.config.settings import MODEL_NAME


# ==========================================================
# LOAD MODEL CONFIGURATION
# ==========================================================

print(f"Loading model: {MODEL_NAME}")


# ==========================================================
# LOAD TOKENIZER
# ----------------------------------------------------------
# The tokenizer converts:
#
# Text
#   ↓
# Tokens
#
# which the model can understand.
# ==========================================================

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)


# ==========================================================
# LOAD MODEL
# ----------------------------------------------------------
# The model performs inference and generates
# responses based on prompts.
# ==========================================================

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)


print("Model loaded successfully.")