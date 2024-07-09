import streamlit as st

st.title("Handbook")
with st.expander("class1-1"):
    st.markdown(
        """
    # class1 notebook
    ```python
    print("hihi")  # 在終端機中輸出
    print("hello" + " " + "world")  # 在終端機中輸出
    print("hi " * 10)
    name = "python"
    age = 31
    print(name, age)
    print(f"i am {name} and i am {age} years old")
    print(len(name))
    print(type(name))

    int() 函數可以將 不同的資料型別轉換為 int 型別。
    float() 函數可以將 不同的資料型別轉換為 float 型別。
    str() 函數可以將 不同的資料型別轉換為 str 型別。
    bool() 函數可以將 不同的資料型別轉換為 bool 型別。

    # print("可以把輸入的資料存起來")
    # a = input("隨便輸入:")
    # print(a)

    age = int(input("請輸入您的年齡:"))
    print("您的年齡是:", age)
    ```
    """
    )


with st.expander("class1-2"):
    st.markdown(
        """# Streamlit 筆記

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
    '''
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
    '''
)

```
# 按鈕事件
使用 `st.button` 來建立一個按鈕，當按鈕被點擊時，會顯示氣球動畫。

```python
if st.button("click me"):
    st.balloons()

```
"""
    )


with st.expander("class2-1"):
    st.markdown(
        """
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

   """
    )


with st.expander("class2-2"):
    st.markdown(
        """
        
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
 """
    )


with st.expander("class1-5"):
    st.markdown(
        """
# 程式技巧筆記

## 使用的程式技巧

### 1. import 語句

import 語句用於引入外部模組或函式庫，以便在程式中使用其功能。

```python
import streamlit as st
```

這行程式碼引入了 streamlit 模組，並將其簡稱為 st，方便在程式中使用。

### 1. for 迴圈

for 迴圈用於重複執行一段程式碼，迴圈次數由 range 函式決定。

```python

  for i in range(10):
      st.markdown("hihi")
```

這個迴圈會執行 10 次，每次都會使用 streamlit 的 markdown 方法輸出 "hihi"。

### 1. range 函式

range 函式生成一個數字序列，常用於控制迴圈的次數。

```python
  for i in range(10):
      st.markdown(i)
```

這個迴圈會執行 10 次，每次迴圈變數 i 的值從 0 到 9，並且每次都會使用 streamlit 的 markdown 方法輸出 i 的值。

### 1. range 函式的變體

range 函式可以接受多個參數來控制序列的開始、結束和步長。

```python
  for i in range(1, 10):
      st.markdown(i)
```

這個迴圈會執行 9 次，每次迴圈變數 i 的值從 1 到 9，並且每次都會使用 streamlit 的 markdown 方法輸出 i 的值。

```python
  for i in range(1, 10, 2):
      st.markdown(i)
```

這個迴圈會執行 5 次，每次迴圈變數 i 的值從 1 開始，每次增加 2，直到小於 10，並且每次都會使用 streamlit 的 markdown 方法輸出 i 的值。

### 1. streamlit 的 markdown 方法

streamlit 的 markdown 方法用於在網頁上顯示 Markdown 格式的文字。

```python
  st.markdown("hihi")
```

這行程式碼會在網頁上顯示 "hihi"。

```python
  st.markdown(i)
```

這行程式碼會在網頁上顯示變數 i 的值。    
"""
    )
with st.expander("class1-6"):
    st.markdown(
        """
# Streamlit 程式技巧筆記

### 引入模組
```python
import streamlit as st: 
```

引入 streamlit 模組，並將其名稱縮寫為 st，方便後續使用。

```python
number = int(
    st.number_input("請輸入一個數字", step=1, max_value=9, min_value=1, value=1)
```

- st.number_input：這是一個 Streamlit 提供的函數，用於在網頁上顯示一個數字輸入框。
- "請輸入一個數字"：輸入框的提示文字。
- step=1：每次增加或減少的步長。
- max_value=9：輸入的最大值。
- min_value=1：輸入的最小值。
- value=1：預設值。
- int(...)：將輸入的數字轉換為整數型別。

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
"""
    )
