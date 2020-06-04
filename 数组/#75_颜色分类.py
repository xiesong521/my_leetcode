#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
def sortColor(nums):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

def sortColor2(nums):
    begin = current = 0
    end = len(nums) - 1
    while end >= current:
        if nums[current] == 2:
            nums[current], nums[end] = nums[end], nums[current]
            end -= 1
        elif nums[current] == 0:
            nums[current], nums[begin] = nums[begin], nums[current]
            begin += 1
            current += 1
        else :
            current += 1
    return nums

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    sortnum = sortColor2(nums)
    print(sortnum)
