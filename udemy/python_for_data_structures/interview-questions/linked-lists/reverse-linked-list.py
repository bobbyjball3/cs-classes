#! /usr/bin/env python3

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None

def reverseLinkedList(node):
    currentNode = node
    previousNode = None
    nextNode = None

    # Edge case for list with one node
    if currentNode.nextNode == None:
        return currentNode

    # Loop until currentNode is None (signalling we reached the end of the list)
    while currentNode:
        nextNode = currentNode.nextNode
        currentNode.nextNode = previousNode
        previousNode = currentNode
        currentNode = nextNode

    return previousNode

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextNode = b
b.nextNode = c
c.nextNode = d

# Prints values 1,2,3,4
print(a.value)
print(a.nextNode.value)
print(b.nextNode.value)
print(c.nextNode.value)

# Reverse the linked list
reverseLinkedList(a)

# Prints values 4,3,2,1
print(d.value)
print(d.nextNode.value)
print(c.nextNode.value)
print(b.nextNode.value)
