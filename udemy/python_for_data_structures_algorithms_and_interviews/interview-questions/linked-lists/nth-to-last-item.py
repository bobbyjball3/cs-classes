#! /usr/bin/env python3

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None


# O(N), but uses more memory
def nth_to_last_node(n, head):
    node = head
    listItemPositions = dict()
    targetNode = None
    itemPosition = 1

    while node:
        listItemPositions[itemPosition] = node
        itemPosition += 1
        node = node.nextnode

    targetNode = listItemPositions[itemPosition - n]

    return targetNode

# second attempt, still O(N), but uses significantly less memory
def nth_to_last_node_2(n, head):
    node = head
    targetNode = head
    marker = 1
    currentPosition = 1

    while node:
        if (currentPosition - marker) == n:
            targetNode = targetNode.nextnode
            marker += 1
        
        currentPosition += 1
        node = node.nextnode

    return targetNode


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a) 
print(target_node.value)

target_node_2 = nth_to_last_node_2(2, a) 
print(target_node_2.value)