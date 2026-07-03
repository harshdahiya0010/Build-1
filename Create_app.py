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

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import time

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

# -----------------------------
# LLM
# -----------------------------
model = ChatOpenAI()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
background:linear-gradient(135deg,#0F172A,#1E293B,#111827);
color:white;
}

.big-title{
font-size:55px;
font-weight:700;
text-align:center;
color:white;
margin-top:-20px;
}

.subtitle{
text-align:center;
font-size:20px;
color:#CBD5E1;
margin-bottom:40px;
}

.input-box{
padding:15px;
border-radius:15px;
background:#1E293B;
}

.response-box{
background:#1E293B;
padding:25px;
border-radius:15px;
border-left:6px solid #38BDF8;
margin-top:20px;
box-shadow:0px 0px 15px rgba(0,0,0,.3);
}

div.stButton > button{
background:linear-gradient(90deg,#2563EB,#06B6D4);
color:white;
font-size:18px;
font-weight:bold;
border-radius:12px;
padding:12px;
width:100%;
border:none;
transition:0.3s;
}

div.stButton > button:hover{
transform:scale(1.02);
box-shadow:0px 0px 20px #38BDF8;
}

.css-1d391kg{
background:#111827;
}

hr{
border:1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🤖 Research Assistant")

    st.markdown("---")

    st.markdown("### Features")

    st.write("✅ Powered by GPT")
    st.write("✅ Fast Responses")
    st.write("✅ Research Tool")
    st.write("✅ Clean UI")

    st.markdown("---")

    if st.button("🗑 Clear Output"):
        st.session_state.pop("response", None)

    st.markdown("---")

    st.caption("Created using Streamlit + LangChain")

# -----------------------------
# Hero Section
# -----------------------------
st.markdown("<div class='big-title'>🤖 AI Research Assistant</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Ask anything • Get intelligent responses instantly</div>", unsafe_allow_html=True)

# -----------------------------
# Prompt
# -----------------------------
user_prompt = st.text_area(
    "",
    placeholder="Example:\n\nExplain Quantum Computing in simple words...",
    height=180
)

# -----------------------------
# Button
# -----------------------------
if st.button("🚀 Generate Response"):

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
        st.stop()

    with st.spinner("🧠 Thinking..."):

        time.sleep(1)

        result = model.invoke(user_prompt)

        st.session_state.response = result.content

# -----------------------------
# Output
# -----------------------------
if "response" in st.session_state:

    st.success("Response Generated Successfully")

    st.markdown("## 📄 Response")

    st.markdown(
        f"""
        <div class="response-box">
        {st.session_state.response}
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("<br><hr>", unsafe_allow_html=True)

st.caption("Built with ❤️ using LangChain • OpenAI • Streamlit")
