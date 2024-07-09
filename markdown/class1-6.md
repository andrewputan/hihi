# Streamlit 程式技巧筆記

### 引入模組

import streamlit as st:

```

引入 streamlit 模組，並將其名稱縮寫為 st，方便後續使用。

```python
number = int(
    st.number_input("請輸入一個數字", step=1, max_value=9, min_value=1, value=1)
)
```

st.number_input：這是一個 Streamlit 提供的函數，用於在網頁上顯示一個數字輸入框。
"請輸入一個數字"：輸入框的提示文字。
step=1：每次增加或減少的步長。
max_value=9：輸入的最大值。
min_value=1：輸入的最小值。
value=1：預設值。
int(...)：將輸入的數字轉換為整數型別。

### 迴圈與輸出

```python
for i in range(1, number + 1):
    st.markdown(str(i) * i)
```

- for i in range(1, number + 1)：使用 for 迴圈從 1 遍歷到 number。
- range(1, number + 1)：生成從 1 到 number 的數字序列。
- st.markdown(str(i) * i)：將數字 i 轉換為字串，並重複 i 次，然後使用 st.markdown 在網頁上顯示出來。
- str(i) * i：將數字 i 轉換為字串並重複 i 次，例如 i=3 時，結果為 "333"。
- st.markdown：Streamlit 提供的函數，用於在網頁上顯示 Markdown 格式的文字。
