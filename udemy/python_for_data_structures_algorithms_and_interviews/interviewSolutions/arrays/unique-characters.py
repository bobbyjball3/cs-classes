#! /usr/bin/env python3

def uni_char(s):
  if s == '':
    return True

  charsPresent = set()
  chars = list(s)

  for char in chars:
    if char in charsPresent:
      return False
    else:
      charsPresent.add(char)

  return True



print(uni_char('goo'))
print(uni_char(''))
print(uni_char('abcdefg'))