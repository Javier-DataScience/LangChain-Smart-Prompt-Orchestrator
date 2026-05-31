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
# - Make model upgrades easier (via settings.py)
#
# ARCHITECTURE:
#
# settings.py
#      ↓
# model_loader.py
#      ↓
# chains/
#      ↓
# FastAPI (later layer)
#
# ==========================================================

from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM
)

from src.config.settings import MODEL_NAME


# ==========================================================
# MODEL INITIALIZATION START
# ==========================================================

print("=" * 50)
print(f"Loading model: {MODEL_NAME}")
print("=" * 50)


# ==========================================================
# LOAD TOKENIZER
# ----------------------------------------------------------
# Converts raw text into tokens (numbers) that the model understands.
#
# Example:
# "machine learning"
#        ↓
# [2315, 98, 1200]
#
# This step is REQUIRED for HuggingFace models.
# ==========================================================

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)


# ==========================================================
# LOAD MODEL
# ----------------------------------------------------------
# The model performs inference:
#
# Tokens → Neural Network → Generated Tokens → Text
#
# This is the "brain" of the system.
# ==========================================================

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)


# ==========================================================
# MODEL READY
# ==========================================================

print("Model loaded successfully ✔")