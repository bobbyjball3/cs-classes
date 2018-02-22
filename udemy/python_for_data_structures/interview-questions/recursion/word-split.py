#! /usr/bin/env python3

# This is a very naive implementation. If the order of the words in the phrase is not just right, the algorithm fails...
# It's actually almost a graph building problem, where the graph's nodes are instances of words found at the start, branching from there
def word_split(phrase,list_of_words, output = None):
  phrase = phrase.strip()
  
  if output == None:
    output = []

  for word in list_of_words:
    if phrase.startswith(word):
      output.append(word)
      phrase = phrase.replace(word, '', 1)
      return word_split(phrase, list_of_words, output)
    
  
  return output



# Outputs []
print(word_split(' ',['the','ran','man']))

# Outputs ['the', 'man', 'ran']
print(word_split('themanran',['the','ran','man']))

# outputs: ['i', 'love', 'dogs', 'John']
print(word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John']))

# outputs: []
print(word_split('themanran',['clown','ran','man']))

# Known failure case. Prints [ "the" ] instead of [ "then", "name" ]
print(word_split("thenname", [ "the", "then", "name" ]))