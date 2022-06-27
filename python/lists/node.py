#!/usr/bin/env python3

# Sample demo of Node object

class Node:
   #Initialize node object
   def __init__(self, data, next=None):
       self.data = data
       self.next = None
   
first = Node(100)
print(first.data)

# A single node of a singly linked list
class Node1:
  # constructor
  def __init__(self, data, next=None): 
    self.data = data
    self.next = next

# Creating a single node
first = Node1(3)
print(first.data)
