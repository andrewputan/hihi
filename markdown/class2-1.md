# 程式技巧筆記

以下是一些在程式中使用的基本比較操作和條件判斷的相關知識：

## 比較操作

在程式中，我們經常需要比較數值或變數之間的大小關係。以下是一些常用的比較操作：

```python
import streamlit as st

st.markdown(1 == 1)  # 比較有沒有相等
st.markdown(1 != 0)  # 比較有沒有不相等
st.markdown(1 < 2)  # 比較是否小於
st.markdown(1 > 2)  # 比較是否大於
st.markdown(1 <= 2)  # 比較是否小於或等於
st.markdown(1 >= 2)  # 比較是否大於或等於
```

- `==`：檢查兩個值是否相等。例如，1 == 1 會回傳 True。
- `!=`：檢查兩個值是否不相等。例如，1 != 0 會回傳 True。
- `<`：檢查左邊的值是否小於右邊的值。例如，1 < 2 會回傳 True。
- `>`：檢查左邊的值是否大於右邊的值。例如，1 > 2 會回傳 False。
- `<=`：檢查左邊的值是否小於或等於右邊的值。例如，1 <= 2 會回傳 - True。
- `>=`：檢查左邊的值是否大於或等於右邊的值。例如，1 >= 2 會回傳 False。

## 條件判斷

- 條件判斷是程式中非常重要的一部分，它可以根據不同的條件執行不同的程式碼。以下是一個使用條件判斷來檢查密碼是否正確的範例：

```python
password = st.text_input("請輸入密碼:")
if password == "hihi":
    st.markdown("密碼正確")
elif password == "hihihi":
    st.markdown("密碼正確")
elif password == "hi":
    st.markdown("密碼正確")
else:
    st.markdown("密碼錯誤")
```

- if：如果條件為真，則執行對應的程式碼塊。例如，當 password == "hihi" 時，會顯示 "密碼正確"。
- elif：表示 "else if"，如果前面的條件不成立，則檢查這個條件。例如，當 password == "hihihi" 時，會顯示 "密碼正確"。
- else：如果所有前面的條件都不成立，則執行 else 塊中的程式碼。例如，當密碼不等於 "hihi"、"hihihi" 或 "hi" 時，會顯示 "密碼錯誤"。
