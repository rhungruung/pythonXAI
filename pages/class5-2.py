import streamlit as st
import os

st.title("圖片元件")
# st.image只另,參數(圖片檔案路徑, 寬度)
st.image("image/banana.png", width=300)

import_folder = "image"  # 資料名稱
image_files = os.listdir(import_folder)  # 取得資料夾中所有檔案
st.write(image_files)  # 顯示所有檔案
# 例如: ['banana.png', 'apple.png', 'orange.png']

image_size = st.number_input("圖片大小", min_value=50, max_value=500, value=100)

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{import_folder}/{image_file}", width=300)
    # 顯示圖片, 根據使用者輸入的大小調整寬度

for image_file in image_files:
    # 除了width, 還有use_column_width可以使用,會將圖片寬度設為容器寬度
    st.image(f"{import_folder}/{image_file}", use_container_width=True)
    # 顯示圖片, 根據使用者輸入的大小調整寬度


# 下拉選單選擇要顯示的圖片
selected_image = st.selectbox("選擇圖片", image_files)
st.image(f"{import_folder}/{selected_image}", width=500)
