# 程式技巧筆記

## 1. 匯入模組 (import module)

```python
import random  # 匯入 random 模組
2. 隨機數 (random)
python
Copy
ans = random.randint(1, 100)  # 隨機產生 1 到 100 的整數
3. 無窮迴圈 (infinite loop)
python
Copy
while True:  # 無窮迴圈
    # 迴圈內的程式碼將不斷執行，直到遇到 break
4. 使用者輸入 (user input)
python
Copy
num = int(input("請輸入 1 到 100 的整數："))  # 使用者輸入 1 到 100 的整數
5. 條件判斷 (conditional statements)
python
Copy
if num < 0 or num > 100:
    print("請輸入1到100的整數")
elif num > ans:  # 如果 num 大於 ans
    print("太大了！")
elif num < ans:  # 如果 num 小於 ans
    print("太小了！")
else:  # 如果 num 等於 ans
    print("答對了！")
    break  # 跳出迴圈
6. 跳出迴圈 (break)
python
Copy
break  # 當 num 等於 ans 時跳出迴圈
完整範例程式
python
Copy
import random

ans = random.randint(1, 100)  # 隨機產生 1 到 100 的整數

while True:  # 無窮迴圈
    num = int(input("請輸入 1 到 100 的整數："))  # 使用者輸入 1 到 100 的整數
    if num < 0 or num > 100:
        print("請輸入1到100的整數")
    elif num > ans:  # 如果 num 大於 ans
        print("太大了！")
    elif num < ans:  # 如果 num 小於 ans
        print("太小了！")
    else:  # 如果 num 等於 ans
        print("答對了！")
        break  # 跳出迴圈
