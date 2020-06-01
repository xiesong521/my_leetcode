#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# 例如：
# 输入：[2，3，1，0，2，5，3]
# 输出：2或3
# 方法1：
# 新建一个数组，依次判断给定数组中的元素，是否在新数组中，不在就添加，在就输出


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if numbers == []:
            return False
        for i in range(len(numbers)-1):
            if numbers[i] < 0 or numbers[i]>len(numbers)-1:
                return False
        for i in range(len(numbers)-1):
            while(numbers[i] != i):
                if numbers[i]== numbers[numbers[i]]:
                    duplication[0] = numbers[i]
                    return True
                else:
                    temp = numbers[i]
                    numbers[i] = numbers[temp]
                    numbers[temp] = temp
        return False