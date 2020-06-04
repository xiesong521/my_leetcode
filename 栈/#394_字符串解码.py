#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""




if __name__ == '__main__':
    s = '100[leetcode]'
    res = ''
    num = 0
    stack = [] # 用元组的方式记录'['外的数字和之前的字符
    for c in s:
        if c == '[':
            stack.append((num,res))
            num, res = 0, ''
        elif c.isdigit():
            num = num * 10 + int(c)  # 不能只考虑个位数
        elif c == ']':
            top = stack.pop()
            res = top[1] + res * top[0]
        else:
            res += c
    print(res)

    # for str   in stack:
    #     res += str
    # print(res)



