#! /usr/bin/env python3
from operator import itemgetter

def memoize(functionToMemoize):

    cache = {}

    def memoizedFunction(target, coins):
        cacheKey = str(target) + '::' + ",".join(str(coin) for coin in sorted(coins))
        if cacheKey not in cache:
            cache[cacheKey] = functionToMemoize(target, coins)

        return cache[cacheKey]
    
    memoizedFunction.cache = cache
    return memoizedFunction

@memoize
def rec_coin(target,coins):

    minCoins = target

    # base case
    if target in coins:
        return 1


    for coin in [ c for c in coins if c <= target ]:
        numCoins =  1 + rec_coin( target - coin, coins )
        if numCoins < minCoins:
            minCoins = numCoins

    return minCoins

# Tests
testCases = [ (10, [1,5]), (10, [1,5,10]), (1, [1, 5]), (27, [1, 5]), (27, [1, 5, 10]), (19, [ 1, 5, 10 ]) ]
expectedResults = [ 2, 1, 1, 7, 5, 6 ]
testNumber = 1
for testCase, expectedResult in zip(testCases, expectedResults):
    
    changeAmount, coins = testCase
    result = rec_coin(changeAmount, coins)
    print("\n### Test case {}".format(testNumber))
    print("\t- Test passed? {}".format(result == expectedResult))
    print("\t\t* expected: {}".format(expectedResult))
    print("\t\t* actual:   {}".format(result))

    testNumber += 1