# Streamlit 程式技巧筆記

這是一個使用 Streamlit 的簡單範例程式，展示了如何使用數字輸入和條件判斷來顯示不同的訊息。

## 程式碼範例

```python
import streamlit as st
```

## 數字輸入框

```python
number = st.number_input(
    "請輸入一個數字", step=1, max_value=100, min_value=-100, value=0
)
st.markdown(f"你輸入的數字是 {number}")
st.markdown("---")
```

## 分數輸入框

```python
score = st.number_input("請輸你的分數", step=1, max_value=100, min_value=-100, value=90)
```

## 根據分數顯示等級

```python
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
```

## 程式技巧

匯入 Streamlit 模組：

``` python
Copy
   import streamlit as st
 ```

Streamlit 是一個開源的 Python 庫，可以幫助你快速建立網頁應用程式。

## 數字輸入框

```python

   number = st.number_input(
       "請輸入一個數字", step=1, max_value=100, min_value=-100, value=0)
```

- st.number_input 用於創建數字輸入框。
- step 參數設定每次調整的步伐。
- max_value 和 min_value 設定輸入數字的範圍。
- value 設定預設值。
max_value 和 min_value 設定輸入數字的範圍。
value 設定預設值。
顯示輸入的數字：

```python
   st.markdown(f"你輸入的數字是 {number}")
   st.markdown("---")
   ```

使用 st.markdown 顯示格式化的文字。
條件判斷顯示等級：

```python

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
```

根據輸入的分數，使用 if-elif-else 條件判斷來顯示不同的等級和訊息。
