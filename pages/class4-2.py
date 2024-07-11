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
        break
