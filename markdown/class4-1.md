# 程式技巧筆記

## 1. 條件式迴圈 (while loop)

```python
i = 0
while i < 5:  # 當 i < 5 時執行迴圈
    print(i)
    i += 1  # i = i + 1
2. 算術指定運算子
python
Copy
a = 10
a += 1  # 等同於 a = a + 1
print(a)
a -= 1  # 等同於 a = a - 1
print(a)
a *= 2  # 等同於 a = a * 2
print(a)
a /= 2  # 等同於 a = a / 2
print(a)
a //= 2  # 等同於 a = a // 2
print(a)
a %= 3  # 等同於 a = a % 3
print(a)
a **= 2  # 等同於 a = a ** 2
print(a)
3. 運算子優先順序
() 括號
** 指數
* / // % 乘法、除法、整數除法、取餘數
+ - 加法、減法
== != > < >= <= 比較運算子
not、and、or 邏輯運算子
= += -= *= /= //= %= **= 賦值運算子
4. 跳出迴圈 (break)
使用 while 迴圈
python
Copy
i = 1
while i < 6:  # 當 i < 6 時執行迴圈
    print(i)  # 印出 i
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
    i += 1
使用 for 迴圈
python
Copy
for i in range(1, 6):  # i 從 1 到 5
    print(i)  # 印出 i
    if i == 3:
        break  # 當 i 等於 3 時跳出迴圈
5. 隨機數 (random)
python
Copy
import random  # 匯入 random 模組

print(random.randrange(10))  # 隨機產生 0 到 9 的整數
print(random.randrange(1, 10))  # 隨機產生 1 到 9 的整數
print(random.randrange(1, 10, 2))  # 隨機產生 1 到 9 的奇數
# randrange 跟 range 一樣，第一個數字是開始，第二個數字是結束，第三個數字是間隔
# 不會數到結束的數字，randrange(1, 10) 只會從 1~9 隨機選一個數字

print(random.randint(1, 10))  # 隨機產生 1 到 10 的整數
# randint 跟 randrange 一樣，第一個數字是開始，第二個數字是結束
# 但 randint 一定要設定兩個數字，且會數到結束的數字
