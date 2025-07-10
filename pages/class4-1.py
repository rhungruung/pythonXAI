import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2columns
col1.button("按鈕1", key="button1")  # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="button2")  # 在col2中建立一個按鈕類似st.button("按鈕2")

# 2columns, 可以用比例來設定每個column的寬度,將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕3", key="button3")
col2.button("按鈕7", key="button4")

# 2columns, 可以用比例來設定每個column的寬度,將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕9", key="button5")
col2.button("按鈕8", key="button6")

# 3columns
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕5", key="button7")
col2.button("按鈕6", key="button8")
col3.button("按鈕7", key="button9")

st.write("---")
col1, col2, col3 = st.columns([1, 2, 3])
with col1:  # 在col1中建立一個按鈕類似
    st.button("按鈕8", key="button10")
with col2:  # 在col2中建立一個按鈕類似
    st.button("按鈕9", key="button11")
with col3:  # 在col3中建立一個按鈕類似
    st.write("這是col2")
    st.button("按鈕9", key="button12")

# 多個columns
cols = st.columns(4)  # 4columns, cols[0]...cols[3]
for i in range(len(cols)):
    with cols[i]:
        st.button(f"for當中的按鈕{i+1}", key=f"多col{i+10}")
        # 這邊按鈕的key叫做:多col0, 多col1 ,多col2,多col3
st.write("---")
st.title("columns排列元件效果比較")
# 只開1個row , 2個columns
col1, col2 = st.columns(2)
with col1:
    st.button("按鈕1", key="button13")
    st.button("按鈕2", key="button14")
    st.button("按鈕3", key="button15")
with col2:
    st.write("這是col2")
    st.write("這是col2")
    st.write("這是col2")
st.write("---")
# 開3個row , 2個columns
for i in range(3):
    col1, col2 = st.columns(2)
    with col1:
        st.button(f"按鈕{i+1}", key=f"排版測試{i+4}")
    with col2:
        st.write(f"這是col2{i+1}")
st.write("---")
st.title("文字輸入元件")
# st.text_input指令格式 st.text_input(輸入欄位的標題,value="預設顯示文字")
text = st.text_input("請輸入你的姓名", value="這是預設文字")
st.write(f"你輸入的文字是:{text}")
st.write("---")
st.title("session_state")
ans = 1  # 設定一個變數ans=1
if st.button("按下去ans加1", key="ans1"):  # 如果按下按鈕
    ans = ans + 1  # ans+1
st.write(f"ans={ans}")  # 顯示ans的值

# session_state
if "ans" not in st.session_state:  # 如果session_state中沒有ans這個變數
    st.session_state.ans = 1  # 設定session_state.ans=1

if st.button("按下去ans加1", key="ans2"):
    st.session_state.ans = st.session_state.ans + 1  # session_state.ans+1
st.write(f"ans={st.session_state.ans}")

# 有時候按鈕按下,不一定會重新整理整個畫面
# 這時候可以使用st.rerun()強制重新整理畫面
if st.button("重新整理畫面", key="banana"):  # 如果按下按鈕
    st.rerun()  # 重新執行程式
