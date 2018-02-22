#! /usr/bin/env python3

def balance_check(s):
    # Set of opening parens
    openingParens = set()
    openingParens.add('(')
    openingParens.add('[')
    openingParens.add('{')

    # set of balanced parens
    balancedParens = set()
    balancedParens.add('()')
    balancedParens.add('[]')
    balancedParens.add('{}')

    # Stack for holding opening parens
    parensStack = []

    if len(s) % 2 == 1:
        return False

    if s in balancedParens:
        return True

    if s[0] not in openingParens:
        return False

    for char in s:
        if char in openingParens:
            parensStack.append(char)
        else:
            tmpChar = parensStack.pop()
            parenString = tmpChar + char

            if parenString not in balancedParens:
                return False

    return len(parensStack) == 0

print(balance_check('[]'))
print(balance_check('[])'))
print(balance_check(']{}]'))
print(balance_check('[{}]'))