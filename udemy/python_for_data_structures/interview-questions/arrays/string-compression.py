#! /usr/bin/env python3

# O(n) complexity
def compress(s):
  if s == '':
      return s

  compressedString = ""
  characters = list(s)
  previousChar = characters.pop(0)
  charCount = 1

  for char in characters:

    # Increment character count unless it's a new character
    if char == previousChar:
      charCount += 1
    
    # If it is a character change, add the compressed portion to the compressedString
    else:
      compressedString += "{}{}".format(previousChar, charCount)
      previousChar = char
      charCount = 1

  compressedString += "{}{}".format(previousChar, charCount)

  return compressedString



uncompressedString = 'AAAAABBBBCCCC'
compressedString = compress(uncompressedString)

print( "Uncompressed string: {}".format(uncompressedString) )
print( "Compressed string: {}".format(compressedString) )
print( "Test passed: {}".format(compressedString == 'A5B4C4') )