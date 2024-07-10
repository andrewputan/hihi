# 點餐機程式技巧筆記

這個程式使用了 `Streamlit` 來建立一個簡單的點餐機介面，並包含以下程式技巧：

### 1. 使用 `st.session_state` 保存狀態

`st.session_state` 用來在用戶會話期間保存和共享狀態。這裡我們用它來初始化一個空的購物籃並保存用戶添加的食物項目。

```python
if "shopping_cart" not in st.session_state:
    st.session_state.shopping_cart = []
```

### 2. 使用 st.columns 佈局

st.columns 用來創建多列佈局，使介面更加直觀和有條理。在這裡，我們使用兩列來分別輸入食物和顯示購物籃。

```python
col1, col2 = st.columns([3, 1])
```

### 3. 使用 st.text_input 和 st.button 來接受用戶輸入

st.text_input 用來接受用戶輸入的食物項目，st.button 用來觸發添加和刪除操作。

```python

food_item_add = st.text_input("請輸入你想添加的食物：", key="add")
if col2.button("添加到購物籃"):
    if food_item_add:
        st.session_state.shopping_cart.append(food_item_add)
        st.write(f"{food_item_add} 已經被添加到購物籃！")
```

### 4. 動態生成按鈕和顯示內容

根據購物籃的內容動態生成刪除按鈕和顯示項目。每個刪除按鈕都有唯一的鍵，以確保它們能夠正確地對應到各自的食物項目。

```python

for index in range(len(st.session_state.shopping_cart)):
    item = st.session_state.shopping_cart[index]
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(item)
    with col2:
        if st.button("刪除", key=f"remove_{index}"):
            st.session_state.shopping_cart.pop(index)
            st.success(f"{item} 已經從購物籃中刪除！")
            time.sleep(1)
            st.rerun()  # 重新運行以更新購物籃顯示
```

### 5. 使用 st.rerun 來更新介面

當刪除一個項目後，使用 st.rerun 來重新運行程式，以確保購物籃顯示即時更新。

```python

st.rerun()
```

### 6. 使用 time.sleep 延遲操作

time.sleep 用來在刪除操作後稍作延遲，以便用戶能夠看到刪除成功的消息。

```python

time.sleep(1)
```
