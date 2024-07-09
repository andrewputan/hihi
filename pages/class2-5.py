import streamlit as st

[]  # list 清單
print([])  # 印出list
print([1, 2, 3])  # 印出list
print(["a", "b"])  # 印出list
print(["香蕉", "蘋果", "梨"])  # 印出list

# 不管甚麼都可以裝在list中

l = [1, 2, 3, 4, 5]  # 定義list
l[0]  # 取出list的第一個元素
l[1]  # 取出list的第二個元素
l[2]  # 取出list的第三個元素
l[3]  # 取出list的第四個元素
l[4]  # 取出list的第五個元素

l = ["a", "b", "c"]  # 定義list
for index in range(len(l)):
    print(l[index])


l = ["a", "b", "c"]  # 定義list
for index in range(len(l)):
    print(l[index])


l = ["a", "b", "c"]  # 定義list
for element in l:
    print(element)
l = ["a", "b", "c"]  # 定義list
l
l[0] = "A"
print(l[0])

# 這是cow語言的程式碼
L = ["moO", "MOo", "moo", "MoO", "mOo", "MOO"]
L[0] = "moo"
