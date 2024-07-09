import streamlit as st

st.markdown(1 == 1)  # 比較有沒有相等
st.markdown(1 != 0)  # 比較有沒有不相等
st.markdown(1 < 2)  # 比較是否小於
st.markdown(1 > 2)  # 比較是否大於
st.markdown(1 <= 2)  # 比較是否小於或等於
st.markdown(1 >= 2)  # 比較是否大於或等於


password = st.text_input("請輸入密碼:")
if password == "hihi":
    st.markdown("密碼正確")
elif password == "hihihi":
    st.markdown("密碼正確")
elif password == "hi":
    st.markdown("密碼正確")
else:
    st.markdown("密碼錯誤")
