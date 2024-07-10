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

cols = st.columns([1, 5, 1])  # 3個欄位#1比5比1
cols[0].button("按鈕1", key="1")  # 左邊按鈕
cols[1].button("按鈕2", key="2")  # 中間按鈕
cols[2].button("按鈕3", key="3")  # 右邊按鈕


st.title("文字輸入元件")
text = st.text_input("輸入文字")
st.markdown(f"你輸入的文字是：{text}")

st.title("session_state")
ans = 1
st.markdown(f"##### {ans}")
if st.button("按鈕", key="btn"):  # 如果按鈕有按下,頁面會刷新
    ans += 1  # ans = ans + 1
st.markdown(f"##### {ans}")

if "ans" not in st.session_state:  # 如果session_state中沒有ans,就建立一個
    st.session_state.ans = 1  # 建立一個ans的值為1
if st.button("session_state按鈕", key="session_state_btn"):
    st.session_state.ans += 1  # 將session_state的ans值加1,ans可以一直加
st.markdown(f"##### {st.session_state.ans}")
