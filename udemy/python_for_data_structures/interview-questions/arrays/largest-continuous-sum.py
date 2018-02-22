#! /usr/bin/env python3

# My solution, which tracks starting and ending index
def large_cont_sum(arr): 
    startIndex = 0 # Track the starting index for the sum
    endIndex = 0 # Track the ending index for the sum
    maxIndex = len(arr) # max index for range()
    runningSum = 0 # Running sum of numbers
    maxSum = 0

    for index in range(0, maxIndex):
      
      # Catch empty array
      if len(arr) == 0:
        return 0

      # If our sum is already zero, and the current value brings us below zero, we can ignore it
      if runningSum == 0 and arr[index] < 0:
        startIndex = index + 1

      else:
        runningSum += arr[index]

      if runningSum > maxSum:
        endIndex = index
        maxSum = runningSum

    print("Starting index: {}".format(startIndex))
    print("Ending index: {}".format(endIndex))
    
    return maxSum


largestSum = large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
expected = 29
message = "The largest continuous sum is: {}"\
  .format( largestSum ) # Should equal 29

print(message)
print("Passed: {}".format(expected == largestSum))

print("\n\n")

largestSum = large_cont_sum([-1,1,2,3,4,10,10,-10,-1])
expected = 30
message = "The largest continuous sum found is: {}"\
  .format( largestSum ) # Should equal 30

print(message)
print("Passed: {}".format(expected == largestSum))