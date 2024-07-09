import streamlit as st  # 引入 streamlit 模組, 將名稱重新取為 st

number = int(
    st.number_input("請輸入一個數字", step=1, max_value=9, min_value=1, value=1)
)
for i in range(1, number + 1):
    st.markdown(str(i) * i)

numbers = st.number_input("請輸入箭頭大小: ", step=1, min_value=1)
# numbers = int(input("請輸入箭頭大小: "), step=1, min_value=1)
arrow = ""
for i in range(1, numbers * 2, 2):
    # print(" " * ((number * 2 - i) // 2) + "*" * i)
    arrow += " " * ((numbers * 2 - i) // 2) + "*" * i + "\n"
for i in range(numbers):
    # print(" " * (number - 1) + "*")
    arrow += " " * (numbers - 1) + "*" + "\n"
st.markdown(
    f"""
    ```\n這是箭頭金字塔:\n{arrow}\n```
    """
)
