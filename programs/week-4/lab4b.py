# Lab 4.2

def ReverseDuplicator(string):
  pile = ""
  for letter in string:
    pile = letter + letter + pile
  return pile