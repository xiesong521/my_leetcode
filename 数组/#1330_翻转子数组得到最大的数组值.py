#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
#给你一个整数数组nums. 数组值定义为所有满足0<=i<nums.length-1的|nums[i]-nums[i+1]|的和
#你可以选择给定数组的任意子数组，并将该子数组翻转，但你只能执行这个操作一次。
#请你找到可行的最大数组值
#输入nums = [2,3,1,5,4]
#输出10
#解释：通过反转子数组【3，1，5】，数组变成【2，5，1，3，4】，数组值为|2-5|+|5-1|+|1-3|+|3-4|=10