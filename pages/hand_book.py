import streamlit as st
import os

folderPath = "markdown" #設定資料夾
files = os.listdir(folderPath) #取得資料夾下的所有檔案
print(files)

files.sort()  # 將清單排序 , 預設是由小到大

files.sport()  # 將清單排序 , 預設是由小到大

for file in files:  # 將清單排序 , 預設是由小到大

for f in files: # 將清單排序 , 預設是由小到大

for file in files: # ['class1.md', 'class2.md']逐一讀取所有 .md 檔案
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        content = file.read()
    with st.expander(f[:-3]):  #使用expander,標題為檔案名稱去掉.md
        st.markdown(content) # 將檔案內容顯示在網頁上