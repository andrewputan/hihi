# Streamlit 筆記

這段程式碼使用了 `streamlit` 模組，並將它重新命名為 `st`。

```python
import streamlit as st  # 引入 streamlit 模組, 將名稱重新取為 st
```
## 設定標題
使用 `st.title` 來設定頁面的標題。
```python
st.title("this is a title")  # 設定標題
```
## 輸出文字
使用 `st.write` 來輸出文字到頁面。

```python

st.write(
    "this is `st.write`, a function to write text to the page"
)  # 使用 st.write 輸出文字

```
使用 `st.text` 來輸出文字到頁面。

```python

st.text(
    "this is `st.text`, a function to write text to the page"
)  # 使用 st.text 輸出文字

```
輸出 Markdown
使用 `st.markdown` 來輸出 Markdown 格式的內容到頁面。

```python

st.markdown(
    "this is `st.markdown`, a function to write markdown to the page"
)  # 使用 st.markdown 輸出 markdown

```
## Markdown 範例
這段程式碼展示了如何使用 `st.markdown` 來輸出不同層級的標題、列表和程式碼區塊。

```python
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
\```
    """
)

```
# 按鈕事件
使用 `st.button` 來建立一個按鈕，當按鈕被點擊時，會顯示氣球動畫。

```python
if st.button("click me"):
    st.balloons()

```