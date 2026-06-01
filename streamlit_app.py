# ==========================================================
# FILE: streamlit_app.py
# ----------------------------------------------------------
# PURPOSE:
# ChatGPT-like UI for Smart Prompt Orchestrator.
#
# WHY THIS EXISTS:
# Provide a clean conversational interface
# for interacting with the FastAPI backend.
#
# ARCHITECTURE:
#
# User
#   ↓
# Streamlit UI
#   ↓
# FastAPI Backend
#   ↓
# Router
#   ↓
# Chains
#   ↓
# Model
#
# FEATURES:
# - ChatGPT-style interface
# - Typing effect simulation
# - Stable rendering
# - No duplicated messages
# - Docker-ready configuration
#
# DOCKER SUPPORT:
#
# Local:
# http://127.0.0.1:8000/route
#
# Docker:
# http://fastapi:8000/route
#
# Controlled through environment variables.
# ==========================================================

import os
import time
import requests
import streamlit as st


# ==========================================================
# CONFIGURATION
# ----------------------------------------------------------
# Allows different API URLs for:
#
# - Local development
# - Docker containers
# ==========================================================

API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000/route"
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Smart Prompt Orchestrator",
    page_icon="🧠",
    layout="centered"
)


# ==========================================================
# SESSION STATE
# ----------------------------------------------------------
# Stores chat history across reruns.
# ==========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ==========================================================
# HEADER
# ==========================================================

st.title("🧠 Smart Prompt Orchestrator")

st.caption(
    "ChatGPT-style LLM orchestration system"
)


# ==========================================================
# RENDER CHAT HISTORY
# ==========================================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


# ==========================================================
# USER INPUT
# ==========================================================

user_input = st.chat_input(
    "Ask something..."
)


if user_input:

    # ------------------------------------------------------
    # STORE USER MESSAGE
    # ------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

    # ------------------------------------------------------
    # CALL FASTAPI BACKEND
    # ------------------------------------------------------

    try:

        response = requests.post(
            API_URL,
            json={"text": user_input},
            timeout=60
        )

        if response.status_code == 200:

            assistant_response = response.json().get(
                "response",
                ""
            )

        else:

            assistant_response = (
                f"Backend error: "
                f"{response.status_code}"
            )

    except Exception as e:

        assistant_response = (
            f"Connection error: {str(e)}"
        )

    # ------------------------------------------------------
    # TYPING EFFECT
    # ------------------------------------------------------

    with st.chat_message("assistant"):

        placeholder = st.empty()

        typed_text = ""

        for char in assistant_response:

            typed_text += char

            placeholder.markdown(
                typed_text
            )

            time.sleep(0.01)

    # ------------------------------------------------------
    # STORE ASSISTANT MESSAGE
    # ------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )