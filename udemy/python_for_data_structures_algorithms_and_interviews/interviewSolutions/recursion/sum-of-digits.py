#! /usr/bin/env python3

# Non-recursive solution
def sum_func(n):
    
  if n == 0:
    return 0

  nums = str(n)
  sum = 0
  for num in nums:
    sum += int(num)
    
  return sum

# Recursive solution
def sum_func_recursive(n):
    
  if n == 0:
    return 0

  return (n % 10) + sum_func_recursive(int(n/10))


# Non-recursive results
print("Sum of the digits of 4321 is: {}".format(sum_func(4321))) # Should output 10
print("Sum of the digits of 64321 is: {}".format(sum_func(64321))) # Should output 16

# Recursive results
print("Sum of the digits of 4321 is: {}".format(sum_func_recursive(4321))) # Should output 10
print("Sum of the digits of 64321 is: {}".format(sum_func_recursive(64321))) # Should output 16