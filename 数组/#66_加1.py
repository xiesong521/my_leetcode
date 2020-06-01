#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
def plusOne(list):
    for i in range(len(list)-1,-1,-1):
        if list[i] != 9:
            list[i] += 1
            return list
        else:
            list[i] = 0
            if list[0] == 0:
                list.insert(0, 1)
                return list


if __name__ == '__main__':
    list = [9]
    a = plusOne(list)
    print(a)