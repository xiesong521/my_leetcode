#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
import random
# method 1
# class RandomizedSet:
#     def __init__(self):
#         self.array = []
#     def insert(self, val: int) -> bool:
#         if self.array.count(val)== 0:
#             self.array.append(val)
#             return True
#         return False
#     def remove(self, val: int) -> bool:
#         if self.array.count(val)== 0:
#             return False
#         del self.array[self.array.index(val)]
#         return True
#     def getRandom(self) -> int:
#         length = len(self.array)
#         retnum = random.randint(0,length-1)
#         return self.array[retnum]

# method 2

class RandomizedSet:
    def __init__(self):
        self.dict = {}
    def insert(self, val: int) -> bool:
        count = self.dict.get(val,0)
        if count == 0:
            self.dict[val] = 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        count = self.dict.get(val,0)
        if count == 0:
            return False
        else:
            del self.dict[val]
            return True

    def getRandom(self) -> int:
        keys = list(self.dict.keys())
        retnum = random.randint(0,len(keys)-1)
        return keys[retnum]
s = RandomizedSet()

print(s.insert(2))
print(s.insert(3))
print(s.insert(4))
print(s.insert(6))
print(s.insert(7))


print(s.remove(2))
print(s.remove(4))
print(s.getRandom())
