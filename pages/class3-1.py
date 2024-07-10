import streamlit as st

l = [1, 2, 3]  # 在list中加入元素
l.append(4)  # 在list中加入元素
print(l)  # 打印出list

L = ["a", "b", "c", "a"]  # 在list中加入元素
L.remove("a")  # 在list中删除元素
print(L)  # 打印出list
A = [9, 1, -4, 3, 7, 11, 3]  # 在list中加入元素
print(A.count(3))  # 打印出list

L = [3, 12, 7, 9, 5, 3, 3, 3, 2, 4]  # 這個list有10個元素
c = L.count(3)  # 找到3的位置
for i in range(c):
    print(L)

l = [1, 2, 3]

l.pop(0)
print(l)
# pop與remove的差別：pop是用index,remove適用元素來刪除


l = [1, 3, 5, 2, 4]
l.sort()  # 排序
print(l)

l = ["a", "b", "c", "a"]
print(l.index("a"))  # 找到a的位置
