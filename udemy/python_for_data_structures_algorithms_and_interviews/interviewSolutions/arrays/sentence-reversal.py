#! /usr/bin/env python3
import re

def rev_word(s):
    s = s.strip()
    words = re.split(r'\s+', s)
    maxIndex = len(words) - 1
    reversedSentence = []

    for index in range(maxIndex, -1, -1):
      reversedSentence.append(words[index])

    return ' '.join(reversedSentence)

print( rev_word('Hi John,   are you ready to go?') )

print( rev_word('    space before') )