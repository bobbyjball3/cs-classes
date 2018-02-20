#! /usr/bin/env python3

def pair_sum(arr,k):
  seenNumbers = set()
  pairs = set()
  targetSum = k
  
  if len(arr)<2:
    return

  for num in arr:
    secondNumber = targetSum - num
    if secondNumber not in seenNumbers:
      print("Adding number: %d" % secondNumber)
      seenNumbers.add(num)

    else:
      print("Adding pair: {0!s}, {0!s}".format(min(secondNumber, num), max(secondNumber, num)) )
      pairs.add( (min(secondNumber, num), max(secondNumber, num)) )

  return len(pairs)

print("Found {0!s} pair(s)".format(pair_sum([1,3,2,2],4)))
# print(pair_sum([1,2,3,1],3))