#! /usr/bin/env python3

class Node(object):

  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3

# Looping forward over the linked list
currentNode = node1

print("\nForward traversal of linked list")
while currentNode:
  print(currentNode.value)
  currentNode = currentNode.next

# Looping backward over the linked list
currentNode = node4

print("\nBackward traversal of linked list")
while currentNode:
  print(currentNode.value)
  currentNode = currentNode.prev