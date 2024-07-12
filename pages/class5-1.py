import streamlit as st
import time  # 引入時間模組
import os

image_folder = "image"
image_files = os.listdir(image_folder)

if "products" not in st.session_state:
    st.session_state.products = {}
for image_file in image_files:
    product_name = image_file[:-4]
    if product_name not in st.session_state.products:
        st.session_state.products[product_name] = {
            "price": 10,
            "stock": 10,
            "image": f"{image_folder}/{image_file}",
        }
# product 範例
# product = {蘋果:{"prize": 10, "stock": 10, "image": "apple.png"}
#            香蕉:{"prize": 10, "stock": 10, "image": "banana.png"}
#            橘子:{"prize": 10, "stock": 10, "image": "orange.png"}
#            }
st.title("購物平台")
col_num = st.number_input("欄數", min_value=1, max_value=10, value=2)
cols = st.columns(col_num)
i = 0
for product_name, details in st.session_state.products.items():
    with cols[i % col_num]:
        st.image(details["image"], use_column_width=True)
        st.markdown(f"### {product_name}")
        st.markdown(f"價格：${details['price']}")
        st.markdown(f"庫存：{details['stock']}")

        if st.button(f"購買{product_name}", key=f"{product_name}"):
            if details["stock"] > 0:
                st.session_state.products[product_name]["stock"] -= 1
                st.success(f"成功購買{product_name}")
                time.sleep(1)
                st.rerun()
            else:
                st.error(f"庫存不足")
    i += 1


st.title("新增庫存")
product_names = list(st.session_state.products.keys())
col1, col2 = st.columns(2)
with col1:
    selected_product = st.selectbox("選擇商品", product_names)
with col2:
    new_stock = st.number_input("輸入庫存", min_value=1, step=1)
if st.button("新增庫存"):
    st.session_state.products[selected_product]["stock"] += new_stock
    st.success(f"{selected_product}成功新增庫存{new_stock}件")
    time.sleep(1)
    st.rerun()
st.markdown("## 目前庫存")
for product_name, details in st.session_state.products.items():
    st.markdown(f"{product_name}: {details['stock']}件")
