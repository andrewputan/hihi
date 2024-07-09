import streamlit as st

number = st.number_input(
    "請輸入一個數字", step=1, max_value=100, min_value=-100, value=0
)
st.markdown(f"你輸入的數字是 {number}")
st.markdown("---")
score = st.number_input("請輸你的分數", step=1, max_value=100, min_value=-100, value=90)
if score >= 90:
    st.markdown("你的等級是 A")
    st.markdown("你超強")
elif score >= 80:
    st.markdown("你的等級是 B")
    st.markdown("你很強")
elif score >= 70:
    st.markdown("你的等級是 C")
    st.markdown("你還ok")
elif score >= 60:
    st.markdown("你的等級是 D")
    st.markdown("你有點爛")
else:
    st.markdown("你的等級是 F")
    st.markdown("你好爛")
