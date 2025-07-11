import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if "history" not in st.session_state:
    st.session_state.history = []

if "system_message" not in st.session_state:
    st.session_state.system_message = "請用繁體中文進行後續對話"

col1, col2 = st.columns([6, 1])
with col1:
    st.session_state.system_message = st.text_input(
        "系統訊息", st.session_state.system_message
    )
with col2:
    if st.button("清除紀錄"):
        st.session_state.history = []
        st.rerun()

for message in st.session_state.history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="👍").write(message["content"])

prompt = st.chat_input("請輸入你的訊息")
if prompt:
    st.session_state.history.append({"role": "user", "content": prompt})

    response = openai.chat.completions.create(
        model="gpt-4o-mini-search-preview",
        messages=[{"role": "system", "content": st.session_state.system_message}]
        + st.session_state.history,
    )

    assistant_message = response.choices[0].message.content
    st.session_state.history.append({"role": "assistant", "content": assistant_message})
    st.rerun()
