#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
from collections import defaultdict

n = 2
reservedSeats = [[2,1],[1,8],[2,6]]
def maxNumberOfFamilies(n,list):
    left,middle,right = 0b11110000,0b11000011,0b00001111
    occupied = defaultdict(int)

    for seat in reservedSeats:
        if 2 <= seat[1] <= 9:
            occupied[seat[0]] |= (1 << (seat[1] - 2))
    ans = (n-len(occupied)) * 2
    print(occupied)

    for row,bitmask in occupied.items():
        if(bitmask | left )== left or(bitmask | middle) == middle or (bitmask | right) == right:
            ans += 1

    return ans



print(maxNumberOfFamilies(n,reservedSeats))
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# #这里传入的list表示的是list(）函数就是[],也就相当于把字典的所有值赋予初值[],这样子就可以用append了
# d = defaultdict(list)
# for key,value in s:
#     d[key].append(value)
# print(d.items())
#
# nums = [1,3,2,4,1,3,5,2]
# #这里传入的int表示的是int(）函数就是0,也就相当于把字典的所有值赋予初值0,这样子就可以用直接+了
# #可以很方便的统计每一个值出现的次数
# d = defaultdict(int)
# for i in range(len(nums)):
#     d[nums[i]] += 1
# print(d.items())

