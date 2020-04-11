#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 思路   利用target 减去循环的当前数字，看看减后的结果在不在数组中，并且下标不能和当前下标相同
def two_sum(nums,target):
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        if num2 in nums and nums.index(num2)!= i:
            return [i,nums.index(num2)]
    return None

