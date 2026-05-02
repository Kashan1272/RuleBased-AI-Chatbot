import streamlit as st
from chatbot import get_response

# Page config
st.set_page_config(page_title="AI Chatbot", layout="wide")

# Custom CSS for ChatGPT-like UI
st.markdown("""
<style>

/* Background */
body {
    background-color: #0e1117;
}

/* Chat container */
.chat-container {
    max-width: 800px;
    margin: auto;
}

/* User message (bright blue like ChatGPT) */
.user-msg {
    background-color: #2563eb;
    color: white;
    padding: 12px;
    border-radius: 12px;
    margin: 8px;
    text-align: right;
    font-weight: 500;
}

/* Bot message (dark gray contrast) */
.bot-msg {
    background-color: #1f2937;
    color: #e5e7eb;
    padding: 12px;
    border-radius: 12px;
    margin: 8px;
    text-align: left;
}

/* Input box styling */
.stChatInputContainer {
    background-color: #0e1117;
}

/* Remove default white background */
.main {
    background-color: #0e1117;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 ChatGPT-like Rule-Based Chatbot")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat container
chat_container = st.container()

with chat_container:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">{msg["content"]}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Input box at bottom
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate bot response
    response = get_response(user_input)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Rerun to update UI
    st.rerun()