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

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import streamlit as st
from datetime import datetime

# ----------------------------
# Page Config
# ----------------------------

st.set_page_config(
    page_title="Haro AI",
    page_icon="🤖",
    layout="wide"
)

load_dotenv()

model = ChatOpenAI(
    temperature=0.7
)

# ----------------------------
# Custom CSS
# ----------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#090909,#131722,#1B1F2A);
}

.main-title{
    font-size:42px;
    font-weight:800;
    color:white;
}

.sub-title{
    color:#9ca3af;
    font-size:18px;
}

.chat-box{
    border-radius:18px;
    padding:18px;
}

div[data-testid="stChatMessage"]{
    border-radius:18px;
    padding:8px;
}

div[data-testid="stChatMessage"]:hover{
    transform:scale(1.01);
    transition:0.2s;
}

.stChatInput textarea{
    font-size:17px;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Header
# ----------------------------

col1,col2=st.columns([6,1])

with col1:
    st.markdown(
        "<div class='main-title'>🤖 Haro AI</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='sub-title'>Your Personal Intelligent Assistant</div>",
        unsafe_allow_html=True
    )

with col2:

    if st.button("🗑 Clear Chat",use_container_width=True):
        st.session_state.messages=[
            SystemMessage(
                content="""
You are Haro AI.

You are friendly, intelligent,
professional and helpful.

Always answer clearly.
"""
            )
        ]
        st.rerun()

st.divider()

# ----------------------------
# Memory
# ----------------------------

if "messages" not in st.session_state:

    st.session_state.messages=[

        SystemMessage(
            content="""
You are Haro AI.

You are friendly,
professional,
smart,
and helpful.

Remember previous conversation.
"""
        )
    ]

# ----------------------------
# Display Chat
# ----------------------------

for message in st.session_state.messages:

    if isinstance(message,SystemMessage):
        continue

    role="assistant"

    avatar="🤖"

    if isinstance(message,HumanMessage):
        role="user"
        avatar="🧑"

    with st.chat_message(role,avatar=avatar):

        st.markdown(message.content)

# ----------------------------
# Chat Input
# ----------------------------

prompt=st.chat_input("Ask me anything...")

if prompt:

    # Show User Message

    with st.chat_message("user",avatar="🧑"):

        st.markdown(prompt)

        st.caption(datetime.now().strftime("%I:%M %p"))

    # Save User Message

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # AI Thinking

    with st.chat_message("assistant",avatar="🤖"):

        with st.spinner("Thinking..."):

            response=model.invoke(
                st.session_state.messages
            )

            st.markdown(response.content)

            st.caption(datetime.now().strftime("%I:%M %p"))

    # Save AI Response

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )
