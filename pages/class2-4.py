import streamlit as st

# st.number_input()可以讓使用者輸入數字，可以進行以下設定:
# step=1可以讓使用者只能輸入整數
# min_value=0可以讓使用者輸入的數字不能小於0
# max_value=100可以讓使用者輸入的數字不能大於100
number = st.number_input(label="請輸入一個數字", step=1, min_value=0, max_value=100)
# 顯示使用者輸入的數字
st.write(f"你輸入的數字是：{number}")

st.write("---")
st.write("##練習")

score = st.number_input(label="請輸入你的分數", step=1, min_value=0, max_value=100)
if score >= 90:
    st.write("A")
elif score >= 80:
    st.write("B")
elif score >= 70:
    st.write("C")
elif score >= 60:
    st.write("D")
else:
    st.write("F")
