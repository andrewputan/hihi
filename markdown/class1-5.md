# 程式技巧筆記

## 使用的程式技巧

## 1. import 語句

import 語句用於引入外部模組或函式庫，以便在程式中使用其功能。

```python
import streamlit as st
```

這行程式碼引入了 streamlit 模組，並將其簡稱為 st，方便在程式中使用。

## 1. for 迴圈

for 迴圈用於重複執行一段程式碼，迴圈次數由 range 函式決定。

```python

  for i in range(10):
      st.markdown("hihi")
```

這個迴圈會執行 10 次，每次都會使用 streamlit 的 markdown 方法輸出 "hihi"。

## 1. range 函式

range 函式生成一個數字序列，常用於控制迴圈的次數。

```python
  for i in range(10):
      st.markdown(i)
```

這個迴圈會執行 10 次，每次迴圈變數 i 的值從 0 到 9，並且每次都會使用 streamlit 的 markdown 方法輸出 i 的值。

## 1. range 函式的變體

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

## 1. streamlit 的 markdown 方法

streamlit 的 markdown 方法用於在網頁上顯示 Markdown 格式的文字。

```python
  st.markdown("hihi")
```

這行程式碼會在網頁上顯示 "hihi"。

```python
  st.markdown(i)
```

這行程式碼會在網頁上顯示變數 i 的值。
