#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
# import numpy as np
# n,k = input().split()
# n = int(n)
# k = int(k)
# data = []
# for i in range(n):
#     data.append(np.array(list((map(int,input().split())))))
#
# count = 0
# sum = []
# for i in range(n-1):
#     for j in range(i+1,n):
#         for d in range(k):
#             if sum == []:
#                 sum.append(data[i][d] + data[j][d])
#             elif data[i][d] + data[j][d]==sum[-1]:
#                 continue
#             else:
#                 sum.append(data[i][d] + data[j][d])
#         if len(sum) == 1:
#             count = count + 1
#         sum = []
# print(count)


# for i in range(n-1):
#     for j in range(i+1,n):
#         sum_data = np.sum([data[i] + data[j]], axis=0)
#         a = sum_data[0]
#         a_count = list(sum_data).count(a)
#         if a_count == k:
#             count = count + 1

# m,n = input().split()
# m = int(m)
# n = int(n)
# sum = m**n
# a = m * (m-1)**(n-1)
# print(sum-a)

n,m = input().split()
n = int(n)
m = int(m)
c = [0]
w = [0]
m = [-1]
blod = 2
for i in range(n):
    c_,w_ = map(int,input().split())
    c.append(c_)
    w.append(w_)
for i in range(1,n+1):
    if c[i] > blod:
        need_money = (c[i]-blod)//2 +1
        money = m[i-1] - need_money + w[i]
        m.append(money)
        blod = blod + need_money*2-c[i]
    else:
        money = m[i-1] + w[i]
        blod = blod - c[i]
        m.append(money)
print(c)
print(w)
print(max(m))


