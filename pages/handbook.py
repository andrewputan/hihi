import streamlit as st
import os


folderpath = (
    "markdown"  # 這是相對路徑 C:\Users\Michelle\Desktop\hihi\markdown 這是絕對路徑
)
files = os.listdir(folderpath)  # 列出相對路徑

files_name = []  # 建立哦個空的list準備存需要的檔案
for f in files:
    if f.endswith(".md"):  # 如果檔案名稱結尾是.md就加入list
        files_name.append(f)  # 加入files_name的 list中

for f in files_name:  # 遍歷所有markdown檔案的名稱
    with open(f"{folderpath}/{f}", "r", encoding="utf-8") as file:  # 開啟檔案
        content = file.read()  # 讀取檔案內容
    with st.expander(f[:-3]):  # 把.md給刪掉
        st.markdown(content)  # 印出
