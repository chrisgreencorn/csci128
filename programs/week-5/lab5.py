num_list = [66,2,3,7,86,5,9,6,68,12,88]

print 'We begin with the following numbers:'
print num_list

def even_numbers(list):
  for n in list:
    if n % 2 == 0:
      print n

print 'The even numbers in this list are'
even_numbers(num_list)

num_list.remove(7)
index = num_list.index(68)
num_list.insert(index,8)

print 'Removing the number 7, and adding 8 before 68 produces:'
print num_list

num_list.sort()
print 'The above, sorted:'
print num_list

def doubler(list):
  for n in list:
    print n*2
print 'And every number in the list doubled:'
doubler(num_list)
