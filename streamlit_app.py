# ==========================================================
# FILE: streamlit_app.py
# ----------------------------------------------------------
# PURPOSE:
# ChatGPT-like UI for LLM Orchestrator with polished UX
#
# FEATURES:
# - ChatGPT-style message bubbles
# - Typing effect simulation
# - Clean state handling
# - Stable rendering (no duplication)
# ==========================================================

import streamlit as st
import requests
import time


API_URL = "http://127.0.0.1:8000/route"

st.set_page_config(
    page_title="Smart Prompt Orchestrator",
    page_icon="🧠",
    layout="centered"
)

# --------------------------
# SESSION STATE
# --------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------
# HEADER
# --------------------------
st.title("🧠 Smart Prompt Orchestrator")
st.caption("ChatGPT-style LLM orchestration system")

# --------------------------
# RENDER CHAT HISTORY
# --------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --------------------------
# USER INPUT
# --------------------------
user_input = st.chat_input("Ask something...")

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call backend
    response = requests.post(
        API_URL,
        json={"text": user_input}
    )

    if response.status_code == 200:
        assistant_response = response.json().get("response", "")
    else:
        assistant_response = "Error contacting model."

    # --------------------------
    # Typing effect simulation
    # --------------------------
    with st.chat_message("assistant"):
        placeholder = st.empty()
        typed_text = ""

        for char in assistant_response:
            typed_text += char
            placeholder.markdown(typed_text)
            time.sleep(0.01)

    # Store assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_response
    })