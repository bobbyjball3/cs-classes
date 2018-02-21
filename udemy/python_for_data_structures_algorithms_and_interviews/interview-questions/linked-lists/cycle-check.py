#! /usr/bin/env python3

class Node(object):

    def __init__(self, value):
        self.value = value
        self.nextNode = None

def cycleCheck(node):

    currentNode = node
    # checking if an item is in a set is O(N). I could use a dict here to reduce that to O(1)
    # but see the "runner" sollution to 
    visitedNodes = set()

    while True:
        if currentNode.nextNode in visitedNodes:
            return True
        elif currentNode.nextNode == None:
            return False
        else:
            visitedNodes.add(currentNode)
            currentNode = currentNode.nextNode

# Instructor solution
def cycleCheck2(node):

    # Begin both markers at the first node
    marker1 = node
    marker2 = node

    # Go until end of list
    while marker2 != None and marker2.nextNode != None:
        
        # Note
        marker1 = marker1.nextNode
        marker2 = marker2.nextNode.nextNode

        # Check if the markers have matched
        if marker2 == marker1:
            return True

    # Case where marker ahead reaches the end of the list
    return False


a = Node(1)
b = Node(2)
a.nextNode = b
c = Node(3)
b.nextNode = c
d = Node(4)
c.nextNode = d
e = Node(5)
d.nextNode = e
f = Node(6)
e.nextNode = a


print(cycleCheck(a))
print(cycleCheck2(a))