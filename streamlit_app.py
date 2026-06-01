# ==========================================================
# FILE: streamlit_app.py
# ----------------------------------------------------------
# PURPOSE:
# ChatGPT-like UI for LangChain Smart Prompt Orchestrator
#
# WHY THIS EXISTS:
# Provides a clean chat interface over FastAPI backend
#
# KEY FIXES:
# - Prevent duplicate rendering
# - Maintain chat history properly
# - Separate logic from UI rendering
# ==========================================================

import streamlit as st
import requests


# ==========================================================
# CONFIGURATION
# ==========================================================

API_URL = "http://127.0.0.1:8000/route"

st.set_page_config(
    page_title="Smart Prompt Orchestrator",
    page_icon="🧠",
    layout="centered"
)


# ==========================================================
# SESSION STATE (CHAT MEMORY)
# ==========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# ==========================================================
# HEADER
# ==========================================================

st.title("🧠 Smart Prompt Orchestrator")
st.caption("Chat with your LLM system")


# ==========================================================
# DISPLAY CHAT HISTORY (ONLY ONCE)
# ==========================================================

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# ==========================================================
# USER INPUT
# ==========================================================

user_input = st.chat_input("Ask something...")

if user_input:

    # 1. Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # 2. Call backend API
    response = requests.post(
        API_URL,
        json={"text": user_input}
    )

    # 3. Parse response safely
    if response.status_code == 200:
        data = response.json()
        assistant_response = data.get("response", "No response returned")
    else:
        assistant_response = f"Error: {response.status_code}"

    # 4. Store assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_response
    })

    # 5. Rerun to refresh UI properly
    st.rerun()