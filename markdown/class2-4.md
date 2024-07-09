### 使用 st.number_input 函數接收使用者輸入

```python

   number = int(st.number_input("請輸入一個數字", step=1, max_value=9, min_value=1, value=1))
```

- st.number_input 函數用於接收使用者的輸入，並提供一些參數來限制輸入的範圍和步長。
- int 函數將輸入的值轉換為整數。

### 使用 for 迴圈生成輸出

```python
   for i in range(1, number + 1):
       st.markdown(str(i) * i)
```

- for 迴圈用於遍歷從 1 到 number 的範圍，並生成數字金字塔。
- st.markdown 函數用於顯示結果。

## 生成箭頭金字塔

```python
   arrow = ""
   for i in range(1, numbers * 2, 2):
       arrow += " " * ((numbers * 2 - i) // 2) + "*" * i + "\n"
   for i in range(numbers):
       arrow += " " * (numbers - 1) + "*" + "\n"
```

- 使用兩個 for 迴圈來生成箭頭金字塔的上半部分和下半部分。
- 使用字串操作來生成每一行的內容，並將結果累加到 arrow 變數中。

### 顯示箭頭金字塔

```python
   st.markdown(f'''```\n這是箭頭金字塔:\n{arrow}\n```''')
```

- 使用 st.markdown 函數來顯示箭頭金字塔，並使用三重引號來包裹多行字串。
