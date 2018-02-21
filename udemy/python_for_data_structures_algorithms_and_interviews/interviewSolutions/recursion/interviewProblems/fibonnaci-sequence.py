#! /usr/bin/env python3

# An iterrative programming solution
def fib_iter(n):
  prev = 0
  curr = 1

  if n <= 1:
    return n
  
  for i in range(2,n + 1):
    oldCurr = curr
    curr = prev + curr
    prev = oldCurr

  return curr

# A recursive programming solution
def fib_rec(n):

  if n <= 1 and n >= 0:
    return n
  
  return fib_rec(n - 1) + fib_rec(n + 2)

# A dynamic programming solution
def fib_dp(n):

  if n <= 1:
    return n
  
  pass



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
# for testCase, expectedResult in zip(testCases, expectedResults):
#   testNumber += 1
#   result = fib_rec(testCase)
#   print("\n### Test Number {}: {}".format(testNumber, testCase))
#   print("\t- Test case {} passed? {}".format(testCase, result == expectedResult))
#   print("\t\t* Found:    {}".format(result))
#   print("\t\t* Expected: {}".format(expectedResult))

# Dynamic Programming tests
print("\n##################################################")
print("#### Dynamic programming tests")
print("##################################################\n")
testNumber = 0
# for testCase, expectedResult in zip(testCases, expectedResults):
#   testNumber += 1
#   result = fib_dp(testCase)
#   print("\n### Test Number {}: {}".format(testNumber, testCase))
#   print("\t- Test case {} passed? {}".format(testCase, result == expectedResult))
#   print("\t\t* Found:    {}".format(result))
#   print("\t\t* Expected: {}".format(expectedResult))