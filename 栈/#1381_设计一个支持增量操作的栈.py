#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
class CustomStack:

    def __init__(self, maxSize: int):
        self.customStack = []
        self.maxSize = maxSize
        return None
    # def bianli(self):
        for num in self.customStack:
            print(num)


    def push(self, x: int) -> None:
        if len(self.customStack) < self.maxSize:
            self.customStack.append(x)
        return None

    def pop(self) -> int:
        if self.customStack == []:
            return -1
        else:
            top_value = self.customStack[-1]
            del self.customStack[-1]
            return top_value

    def increment(self, k: int, val: int) -> None:
        if len(self.customStack) < k:
            for num in self.customStack:
                num += val
        else:
            for i in range(k):
                self.customStack[i] += val
        for num in self.customStack:
            print(num)



if __name__ == '__main__':
    cu = CustomStack(3)
    print(cu)
    print(cu.push(1))
    print(cu.push(2))
    print(cu.pop())
    print(cu.push(2))
    print(cu.push(3))
    print(cu.push(4))
    print(cu.increment(5,100))
    # print(cu.increment(2,100))



