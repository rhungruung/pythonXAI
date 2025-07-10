import streamlit as st

st.title("點餐機")

if "order" not in st.session_state:
    st.session_state.order = []  # 新增一個購物車的list

col1, col2 = st.columns(2)  # 2欄
with col1:
    foodInput = st.text_input("請輸入餐點")  # 建立一個輸入框
with col2:
    if st.button("加入", key="add"):  # 如果按下按鈕
        st.session_state.order.append(foodInput)  # 把餐點加到購物車

st.write("### 購物車")
for i in range(len(st.session_state.order)):  # 用index來取得購物車中的餐點
    col1, col2 = st.columns(2)  # 2欄
    with col1:
        st.write(st.session_state.order[i])  # 顯示餐點
    with col2:
        if st.button("刪除", key=i):  # 如果按下按鈕, key是index
            st.session_state.order.pop(i)  # 刪除餐點
            # 把購車中的餐點移除,這時候不能用remove,因為remove是用元素來刪除, 因為可能會刪除錯誤的餐點
            st.rerun()  # 重新整理整個畫面
