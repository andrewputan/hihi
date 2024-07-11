# 程式技巧筆記

## 1. 匯入模組 (import module)

```python
import streamlit as st  # 匯入 Streamlit 模組
import os  # 匯入 os 模組
2. Streamlit 基本元件
標題 (Title)
python
Copy
st.title("圖片元件")  # 設定頁面標題
輸出文字 (Write)
python
Copy
st.write(image_files)  # 顯示所有檔案
數字輸入框 (Number Input)
python
Copy
image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)
# 使用者輸入圖片大小, 最小50, 最大500, 預設100, 每次增加50
顯示圖片 (Image)
python
Copy
for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)
    # 顯示圖片, 根據使用者輸入的大小調整寬度

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 顯示圖片, 使用欄寬度
3. 檔案操作 (File Operations)
取得資料夾內所有檔案
python
Copy
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾內所有檔案
完整範例程式
python
Copy
import streamlit as st
import os

st.title("圖片元件")
image_folder = "image"  # 資料夾名稱
image_files = os.listdir(image_folder)  # 取得資料夾內所有檔案
st.write(image_files)  # 顯示所有檔案

image_size = st.number_input("圖片大小", min_value=50, max_value=500, step=50, value=100)
# 使用者輸入圖片大小, 最小50, 最大500, 預設100, 每次增加50

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", width=image_size)
    # 顯示圖片, 根據使用者輸入的大小調整寬度

for image_file in image_files:  # 顯示所有圖片
    st.image(f"{image_folder}/{image_file}", use_column_width=True)
    # 顯示圖片, 使用欄寬度
