"""
------------------------------------------------------------
Project : Haro AI
Author  : Harsh Dahiya
Version : 1.0.0

Description:
A conversational AI chatbot built using Streamlit,
LangChain, and OpenAI GPT.

------------------------------------------------------------
"""

# ==========================
# Imports
# ==========================

import os

import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

# ==========================
# Load Environment Variables
# ==========================

load_dotenv()

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="Haro AI",
    page_icon="🤖",
    layout="centered",
)

# ==========================
# Custom CSS
# ==========================

st.markdown(
    """
    <style>
    .main{
        padding-top:20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================
# Title
# ==========================

st.title("🤖 Haro AI")

st.caption(
    "Your Intelligent AI Assistant powered by OpenAI and LangChain"
)

# ==========================
# API Key Validation
# ==========================

if not os.getenv("OPENAI_API_KEY"):
    st.error("OPENAI_API_KEY not found.")
    st.stop()

# ==========================
# Load LLM
# ==========================

llm = ChatOpenAI(
    temperature=0.7
)

# ==========================
# Session State
# ==========================

if "messages" not in st.session_state:

    st.session_state.messages = [

        SystemMessage(
            content="You are Haro, a helpful AI assistant."
        )

    ]

# ==========================
# Display Chat History
# ==========================

for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.markdown(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.markdown(message.content)

# ==========================
# Chat Input
# ==========================

prompt = st.chat_input("Ask me anything...")

# ==========================
# Chat Logic
# ==========================

if prompt:

    user_message = HumanMessage(content=prompt)

    st.session_state.messages.append(user_message)

    with st.chat_message("user"):
        st.markdown(prompt)

    response = llm.invoke(st.session_state.messages)

    ai_message = AIMessage(content=response.content)

    st.session_state.messages.append(ai_message)

    with st.chat_message("assistant"):
        st.markdown(response.content)

# ==========================
# Sidebar
# ==========================

with st.sidebar:

    st.title("Haro AI")

    st.write("---")

    st.markdown(
        """
### About

Haro AI is a conversational chatbot powered by

- OpenAI GPT
- LangChain
- Streamlit

Created by **Harsh Dahiya**
"""
    )

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = [

            SystemMessage(
                content="You are Haro, a helpful AI assistant."
            )

        ]

        st.rerun()
