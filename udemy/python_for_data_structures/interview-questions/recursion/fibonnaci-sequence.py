#! /usr/bin/env python3

# An iterrative programming solution
def fib_iter(n):
  a, b = 0, 1
  
  # iterrate
  for i in range(n):
    a, b = b, a + b

  return a

# A recursive programming solution
def fib_rec(n):

  # base case
  if n == 1 or n == 0:
    return n
  
  # recurse
  return fib_rec(n-1) + fib_rec(n-2)

# A dynamic programming solution

# Instantiate Cache information
def createCache(n):
  cache = [None] * (n + 1)
  return cache

def fib_dp(n, cache):

  if n <= 1:
    return n
  
  if cache[n] != None:
    return cache[n]
  
  cache[n] = fib_dp(n - 1, cache) + fib_dp(n - 2, cache)
  return cache[n]




#### Tests
testCases = [ 1, 0, 10, 23 ]
expectedResults = [ 1, 0, 55, 28657 ]

# Iterrative tests
print("\n##################################################")
print("#### Iterrative tests")
print("##################################################\n")
testNumber = 0
for testCase, expectedResult in zip(testCases, expectedResults):
  testNumber += 1
  result = fib_iter(testCase)
  print("\n### Test Number {}: {}".format(testNumber, testCase))
  print("\t- Test case {} passed? {}".format(testCase, result == expectedResult))
  print("\t\t* Found:    {}".format(result))
  print("\t\t* Expected: {}".format(expectedResult))



# Recursive tests
print("\n##################################################")
print("#### Recursive tests")
print("##################################################\n")
testNumber = 0
for testCase, expectedResult in zip(testCases, expectedResults):
  testNumber += 1
  result = fib_rec(testCase)
  print("\n### Test Number {}: {}".format(testNumber, testCase))
  print("\t- Test case {} passed? {}".format(testCase, result == expectedResult))
  print("\t\t* Found:    {}".format(result))
  print("\t\t* Expected: {}".format(expectedResult))

# Dynamic Programming tests
print("\n##################################################")
print("#### Dynamic programming tests")
print("##################################################\n")
testNumber = 0
for testCase, expectedResult in zip(testCases, expectedResults):
  testNumber += 1
  cache = createCache(testCase)
  result = fib_dp(testCase, cache)
  print("\n### Test Number {}: {}".format(testNumber, testCase))
  print("\t- Test case {} passed? {}".format(testCase, result == expectedResult))
  print("\t\t* Found:    {}".format(result))
  print("\t\t* Expected: {}".format(expectedResult))