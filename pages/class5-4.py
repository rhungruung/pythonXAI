import streamlit as st

st.chat_message("user").write("這是使用者的訊息")
st.chat_message("assistant").write("這是AI的訊息")

#  範例對話紀錄
history = [
    {"role": "user", "content": "你好"},
    {"role": "assistant", "content": "很開心認識你"},
    {"role": "user", "content": "我是誰"},
    {"role": "assistant", "content": "你就是我"},
]

# 用迴圈顯示聊天泡泡
for message in history:
    if message["role"] == "user":
        st.chat_message("user", avatar="👤").write(message["content"])
    else:
        st.chat_message("assistant", avatar="👍").write(message["content"])
