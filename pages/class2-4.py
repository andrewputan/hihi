import streamlit as st  # 引入 streamlit 模組, 將名稱重新取為 st

number = int(
    st.number_input("請輸入一個數字", step=1, max_value=9, min_value=1, value=1)
)
for i in range(1, number + 1):
    st.markdown(str(i) * i)
