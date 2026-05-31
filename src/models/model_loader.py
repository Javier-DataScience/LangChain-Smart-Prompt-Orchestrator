# ==========================================================
# FILE: model_loader.py
# ----------------------------------------------------------
# PURPOSE:
# Centralize model loading for the entire application.
#
# WHY THIS EXISTS:
# In the notebook, we loaded the Hugging Face model
# multiple times in different cells.
#
# In a real project, the model should be loaded in
# one place only and reused everywhere else.
#
# RESPONSIBILITIES:
# - Load tokenizer
# - Load model
# - Expose both objects to the application
#
# THIS FILE DOES NOT:
# - Create prompts
# - Create chains
# - Route requests
# - Build APIs
# ==========================================================

from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM


MODEL_NAME = "google/flan-t5-small"

print(f"Loading model: {MODEL_NAME}")

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)

print("Model loaded successfully.")