#! /usr/bin/env python3

def reverse(s):
  
  # Return the string if it is 1 or 0 characters
  if len(s) <= 1:
    return s
  
  # Recursively call reverse with a slice of index 1 forward plus the zeroth character
  return reverse(s[1:]) + s[0]

# Prints 'dlrow olleh'
print("Reverse of 'hello world' is: '{}'".format(reverse('hello world')))