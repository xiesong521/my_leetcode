#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.size= 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)
        self.size += 1



    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while(self.stack1) :
            self.stack2.append(self.stack1.pop())
        val = self.stack2.pop()
        while(self.stack2) :
            self.stack1.append(self.stack2.pop())
        self.size -= 1
        return val
    def peek(self) -> int:
        """
        Get the front element.
        """
        while(self.stack1) :
            self.stack2.append(self.stack1.pop())
        val = self.stack2[-1]
        while(self.stack2) :
            self.stack1.append(self.stack2.pop())
        return val

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if self.size == 0:
            return True
        else:
            return False
