# Lab 3.4 program
# Define a function in Python to sum the numbers in the range of two numbers

def sum_of_range(start,end):
  sum = 0
  count = 0
  for num in range(start,end+1):
      sum = sum+num
      count = count+1
#      print count, num, sum
  return sum
