#! /usr/bin/env python3

class Node(object):

  def __init__(self, value):
    self.value = value
    self.next = None

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

# Looping over the linked list
currentNode = node1

while currentNode:
  print(currentNode.value)
  currentNode = currentNode.next