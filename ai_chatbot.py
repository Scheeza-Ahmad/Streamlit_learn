import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# ---------- .env FILE LOAD KARO ----------
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")
st.markdown("Gemini AI se baat karein")

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("Settings")
    if api_key:
        st.success("API Key load ho gayi ✅")
    else:
        st.error("API Key nahi mili. .env file check karein.")
    st.markdown("---")
    if st.button("Chat Clear Karo"):
        st.session_state.messages = []
        st.rerun()

# ---------- SESSION STATE: HISTORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- PURANE MESSAGES DIKHANA ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------- NAYA MESSAGE LENA ----------
user_input = st.chat_input("Apna message likhein...")

if user_input:

    if not api_key:
        st.warning("API key .env file mein set nahi hai.")
        st.stop()

    # 1) User ka message history mein save + dikhao
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # 2) Gemini se response mango
    with st.chat_message("assistant"):
        with st.spinner("Soch raha hoon..."):
            try:
                client = genai.Client(api_key=api_key)
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=user_input
                )
                ai_reply = response.text

                st.write(ai_reply)
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})

            except Exception as e:
                st.error(f"Error: {e}")