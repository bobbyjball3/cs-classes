#! /usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


s = Stack()

print("Is empty? {}".format(s.isEmpty()))
s.push('test')
s.push('testing')
print("Is empty? {}".format(s.isEmpty()))
print("Peek: {}".format(s.peek()))