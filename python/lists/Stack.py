#!/usr/bin/env python3

# Implementation of Stack

class stack():
   def __init__(self):
      self.items = []

   def push(self,item):
      self.items.append(item)

   def pop(self):
       return self.items.pop()   

   def get_stack(self):
       return self.items


myStack = stack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)
myStack.push(50)
myStack.push(60)
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
print(myStack.pop())
