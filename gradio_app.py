# ==========================================================
# FILE: gradio_app.py
# ----------------------------------------------------------
# PURPOSE:
# Gradio interface for the Smart Prompt Orchestrator.
#
# WHY THIS EXISTS:
# Provide an alternative frontend to Streamlit
# while reusing the existing FastAPI backend.
#
# ARCHITECTURE:
#
# User
#   ↓
# Gradio UI
#   ↓
# FastAPI
#   ↓
# Router
#   ↓
# Chains
#   ↓
# Model
#
# BENEFITS:
# - Extremely fast UI development
# - Popular for AI demos
# - Easy Hugging Face Spaces deployment
# - Minimal frontend code
#
# THEME:
# Custom dark theme inspired by ChatGPT.
#
# NOTE:
# This file DOES NOT call the model directly.
# All requests go through FastAPI.
# ==========================================================

import requests
import gradio as gr


# ==========================================================
# CONFIGURATION
# ==========================================================

API_URL = "http://127.0.0.1:8000/route"


# ==========================================================
# CUSTOM DARK CSS
# ==========================================================

CUSTOM_CSS = """
body {
    background-color: #0e1117;
}

.gradio-container {
    background-color: #0e1117 !important;
}

footer {
    visibility: hidden;
}

h1, h2, h3, p, label {
    color: white !important;
}

textarea {
    background-color: #1e1e1e !important;
    color: white !important;
}

input {
    background-color: #1e1e1e !important;
    color: white !important;
}
"""


# ==========================================================
# BACKEND COMMUNICATION
# ==========================================================

def chat_with_ai(message: str):

    try:

        response = requests.post(
            API_URL,
            json={"text": message}
        )

        if response.status_code == 200:

            data = response.json()

            return data.get(
                "response",
                "No response received."
            )

        return f"Error: {response.status_code}"

    except Exception as e:

        return f"Connection error: {str(e)}"


# ==========================================================
# GRADIO INTERFACE
# ==========================================================

demo = gr.Interface(
    fn=chat_with_ai,

    inputs=gr.Textbox(
        lines=3,
        placeholder="Ask something..."
    ),

    outputs=gr.Textbox(
        lines=10
    ),

    title="🧠 Smart Prompt Orchestrator",

    description=(
        "Gradio frontend connected to the "
        "FastAPI backend."
    ),

    css=CUSTOM_CSS
)


# ==========================================================
# APPLICATION ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    demo.launch(
        inbrowser=True
    )