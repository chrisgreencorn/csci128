list1=[1,4,6,9,5,3,0]
num1=3
list2=[9,4,6,9,5,3,2]
num2=9
bin=[]

def biggerThanWithReturn(list,number):
  count=0
  for n in list:
    if n > number:
      bin.append(n)
      count=count+1
  print 'In',list,'the following',count,'numbers are greater than',number,':'
  print bin
  del bin[:]