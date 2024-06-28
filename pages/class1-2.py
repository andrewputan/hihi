import streamlit as st  # 引入 streamlit 模組, 將名稱重新取為 st

st.title("this is a title")  # 設定標題
# 使用 streamlit run 檔案名稱.py
st.write(
    "this is `st.write`, a function to write text to the page"
)  # 使用 st.write 輸出文字
st.text(
    "this is `st.text`, a function to write text to the page"
)  # 使用 st.text 輸出文字
st.markdown(
    "this is `st.markdown`, a function to write markdown to the page"
)  # 使用 st.markdown 輸出 markdown

st.markdown(
    """
# 第一層級標題
## 第二層級標題
### 第三層級標題
#### 第四層級標題
##### 第五層級標題
###### 第六層級標題

- list item 1
- list item 2
- list item 3

1. list item 1
2. list item 2
3. list item 3

```python
print("Hello World")
print('i am andrew')
```
    """
)

if st.button("click me"):
    st.balloons()
