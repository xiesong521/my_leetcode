#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
## 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 给定数组 nums = [1,1,2],
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
# 你不需要考虑数组中超出新长度后面的元素。

# 思路1：
# 如果没有要求空间复杂度为O(1)的话，可以定义一个新的数组，每次遍历原数组，看当前元素是否在新数组中，在就跳过，不在添加
#额外空间是O(1),i首先放在第0个元素上，j从1开始，如果j的元素和i不一样，那么让i+1，j元素的值赋值给i

def removeDuplicates(nums):
    i = 0
    for j in range(1,len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))



#删除列表中元素
# nums = [1,2,3,4,5]
# nums.pop()  #删除最后一个元素5  --》[1,2,3,4]
# nums.pop(2) #删除下标为2的元素3 --》 [1, 2, 4, 5]
# del nums[1] #删除下标为1的元素2  --》 [1, 3, 4, 5]
# del nums[1:3] #删除下标从1到（3-1）的元素 --》 [1, 4, 5]
# nums.remove(5) #删除列表中第一个值为5的元素 --》[1, 2, 3, 4]
# nums.clear()  #删除列表中的所有元素 --》 []
# print(nums)