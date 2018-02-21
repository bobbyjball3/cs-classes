#! /usr/bin/env python3

import math

# This solution did not come easy for me. It still hurts my brain...
# Itertools.permutations does this for you...
def permute(s):
  s = s.strip()
  output = []

  # Base case of string of length 1 or 0
  if len(s) <= 1:
    return [ s ]
  
  # Iterate over every character with an index
  for index, character in enumerate(s):

    # for each permutation of the remaining characters add them to the current character
    for permutation in permute(s[:index] + s[index + 1:]):
      output += [ character + permutation ]

  return output


# Should output expectedResults
testCases = [ 'abc' , 'a' , 'ab', ' ' ]
expectedTestOutputs = [ ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'] , [ 'a' ], [ 'ab', 'ba' ], [ '' ]]
testCaseNumber = 1

for testCase, expectedTestOutput in zip(testCases, expectedTestOutputs):
  results = sorted(permute(testCase))
  
  print("\n### Test case {}: {} ###".format(testCaseNumber, testCase))
  print("\t- Permutation of '{}' passed? {}".format(testCase, results == expectedTestOutput))
  print("\t\t* Found:    {}".format(results))
  print("\t\t* Expected: {}".format(expectedTestOutput))

  testCaseNumber += 1