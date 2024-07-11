# 程式技巧筆記

## 1. 字典 (Dictionary)

### 建立字典

```python
print({})  # 空字典
print({"星期一": "蘋果"})
# 一個 key="星期一"，value="蘋果" 的字典, key 可以是任何不可變的資料型態
print({1: "蘋果", 2: "香蕉"})
# 一個 key=1，value="蘋果" 的字典, key 可以是任何不可變的資料型態
讀取字典
python
Copy
d = {"星期一": "蘋果", "星期二": "香蕉"}
# key 不可重複，value 可以重複
print(d["星期一"])  # 蘋果
2. 字典走訪 (Dictionary Traversal)
python
Copy
d = {"星期一": "蘋果", "星期二": "香蕉"}

# 取得所有的 key
for key in d:
    print(key)
for key in d.keys():
    print(key)
# 以上兩種方式都是取得 key，結果相同

# 取得所有的 value
for value in d.values():
    print(value)  # 蘋果, 香蕉

# 取得所有的 key 和 value
for key, value in d.items():
    print(f"key={key}, value={value}")
for item in d.items():
    print(f"key={item[0]}, value={item[1]}")
3. 元素新增/修改 (Add/Modify Elements)
python
Copy
d = {"星期一": "蘋果", "星期二": "香蕉"}
d["星期一"] = "橘子"  # 修改元素
d["星期三"] = "蘋果"  # 新增元素, 當 key 不存在時會新增元素
print(d)
4. 檢查 key 是否存在 (Check if Key Exists)
python
Copy
d = {"星期一": "蘋果", "星期二": "香蕉"}

# key 是否存在於字典中
print("星期一" in d)  # True
print("星期三" in d)  # False

# value 是否存在於字典中
print("蘋果" in d.values())  # True
print("香蕉" in d.values())  # True

# 檢查 key 是否存在於列表中
L = ["星期一", "星期二"]
print("星期一" in L)  # True
print("星期三" in L)  # False
5. 刪除元素 (Delete Elements)
python
Copy
d = {"星期一": "蘋果", "星期二": "香蕉"}
d.pop("星期一")  # 刪除 key="星期一" 的元素
print(d)
d.pop("星期三", "找不到")  # 如果刪除的元素可能不存在
print(d)
完整範例程式
python
Copy
import random

# 建立字典
print({})  # 空字典
print({"星期一": "蘋果"})
print({1: "蘋果", 2: "香蕉"})

# 讀取字典
d = {"星期一": "蘋果", "星期二": "香蕉"}
print(d["星期一"])  # 蘋果

# 字典走訪
for key in d:
    print(key)
for key in d.keys():
    print(key)
for value in d.values():
    print(value)
for key, value in d.items():
    print(f"key={key}, value={value}")
for item in d.items():
    print(f"key={item[0]}, value={item[1]}")

# 元素新增/修改
d["星期一"] = "橘子"
d["星期三"] = "蘋果"
print(d)

# 檢查 key 是否存在
print("星期一" in d)  # True
print("星期三" in d)  # False
print("蘋果" in d.values())  # True
print("香蕉" in d.values())  # True
L = ["星期一", "星期二"]
print("星期一" in L)  # True
print("星期三" in L)  # False

# 刪除元素
d.pop("星期一")
print(d)
d.pop("星期三", "找不到")
print(d)
