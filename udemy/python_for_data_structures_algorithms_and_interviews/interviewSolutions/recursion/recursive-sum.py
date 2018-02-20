#! /usr/bin/env python3

def rec_sum(n):
    
  if n == 0:
    return 0

  return n + rec_sum(n - 1)

print("Recursive sum of 4 is: {}".format(rec_sum(4))) # Should output 10
print("Recursive sum of 5 is: {}".format(rec_sum(5))) # Should output 15