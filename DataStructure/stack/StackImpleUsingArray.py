# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:20:45 2021

@author: Abeg
"""
class Node: 
    def __init__(self,data): 
        self.data = data
class Stack:   
    def __init__(self): 
        self.array=[]
    def peek(self):
      return self.array[len(self.array)-1]
    def push(self,data):
      self.array.append(data)
    def pop(self,data):
      self.array.pop(data)
    def search(self,element):
      for i in range(0,len(self.array)):
        if self.array[i]==element:
          return i
obj=Stack()
obj.push(5)
obj.push(5)
obj.push(5)
obj.push(5)
obj.push(4)
print(obj.search(4))
print(obj.array)
