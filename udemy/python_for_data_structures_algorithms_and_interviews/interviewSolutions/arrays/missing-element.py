#! /usr/bin/env python3


# My initial solution, which is O(log(N))
def finder(arr1,arr2):
    
  sortedArr1 = sorted(arr1)
  sortedArr2 = sorted(arr2)
  maxIndex = min(len(sortedArr1), len(sortedArr2))
  missingNumber = 0

  for i in range(0, maxIndex):
    if sortedArr1[i] == sortedArr2[i]:
      continue
    else:
      if len(sortedArr1) > len(sortedArr2):
        missingNumber = sortedArr1[i]
      else:
        missingNumber  = sortedArr2[i]
      
      break
    
    
  return missingNumber

# Optimal solution O(N) using XOR from the solution. Very clever
def finder3(arr1, arr2): 
    result=0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        print(result)
        
    return result 

arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]
print("Missing number: {}".format(finder(arr1,arr2)) )
print("Missing number: {}".format(finder3(arr1,arr2)) )

