#! /usr/bin/env python3
import re

def anagram(s1,s2):
  s1 = removeAllWhitespace(s1.lower())
  s2 = removeAllWhitespace(s2.lower())

  if len(s1) != len(s2):
    return False

  if s1 == s2:
    return True
    
  for char in s1:
    if char.isalpha():
      s2 = s2.replace(char,"",1)

  print(s2)
  return len(s2) == 0

def removeAllWhitespace(string):
  return re.sub(r'\s+','', string)

print(anagram('aabbcc','aabbc') == False)