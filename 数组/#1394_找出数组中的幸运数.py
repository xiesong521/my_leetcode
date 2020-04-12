#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
# 在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。
# 给你一个整数数组 arr，请你从中找出并返回一个幸运数。
# 如果数组中存在多个幸运数，只需返回 最大 的那个。
# 如果数组中不含幸运数，则返回 -1 。
# 思路1：
# 创建一个大小为500，值均为0的数组，遍历原数组，将原数组的值和新数组的下标对应，新数组的值代表出现的次数
# 然后遍历新数组，找到key和value相同的值再存到另一个数组中，然后找到这个数组中的最大值

import numpy as np
def findLucky(nums):
    array1 = np.zeros(500)
    for i in range(len(nums)):
        array1[nums[i]] += 1
    array2 = []
    for i in range(len(array1)):
        if i == array1[i]:
            array2.append(i)
    if max(array2)==0:
        return -1
    else:
        return max(array2)


#思路2：
# 上述思路很明显不管数组有多大都得开辟500大小的数组太浪费
# 我们可以利用字典的键值对，key:存储该数字，value:存储出现的次数
#需要对字典的函数熟悉
def findLucky(nums):
    m = dict()
    for x in nums:
        m[x] = m.get(x,0) + 1
    results = -1
    for key,values in m.items():
        if key == values:
            results = max(results,key)
    return results


print(findLucky([1,2,2,3,3,3]))

#字典 items()函数
# dict = {'xiaohua':22,'xiaobai':23}
# print(dict.items())  # -->dict_items([('xiaohua', 22), ('xiaobai', 23)])
# for name,age in dict.items():
#     print(name,age)
#-->
# xiaohua 22
# xiaobai 23