import streamlit as st
import time

# 初始化一個空的購物籃
if "shopping_cart" not in st.session_state:
    st.session_state.shopping_cart = []

# Streamlit 介面
st.title("歡迎來到點餐機！")

# 使用 columns 佈局
col1, col2 = st.columns([3, 1])

# 在第一列輸入食物並添加到購物籃
with col1:
    food_item_add = st.text_input("請輸入你想添加的食物：", key="add")
if col2.button("添加到購物籃"):
    if food_item_add:
        st.session_state.shopping_cart.append(food_item_add)
        st.write(f"{food_item_add} 已經被添加到購物籃！")

# 顯示購物籃並在每個項目旁邊加上刪除按鈕
if not st.session_state.shopping_cart:
    st.write("購物籃是空的！")
else:
    st.write("購物籃裡有：")
    for index in range(len(st.session_state.shopping_cart)):
        item = st.session_state.shopping_cart[index]
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(item)
        with col2:
            if st.button("刪除", key=f"remove_{index}"):
                st.session_state.shopping_cart.pop(index)
                # st.write(f"{item} 已經從購物籃中刪除！")
                st.success(f"{item} 已經從購物籃中刪除！")
                time.sleep(1)
                st.rerun()  # 重新運行以更新購物籃顯示
