import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 兩個欄位
col1.button("按鈕1")
col2.button("按鈕2")
with col1:
    st.markdown("欄位1")
    st.button("左邊按鈕")
with col2:
    st.markdown("欄位2")
    st.button("右邊按鈕")

cols = st.columns(3)  # 3個欄位
cols[0].button("按鈕1", key="1")  # 左邊按鈕
cols[1].button("按鈕2", key="2")  # 中間按鈕
cols[2].button("按鈕3", key="3")  # 右邊按鈕
