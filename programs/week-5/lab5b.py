list1 = [1,4,6,9,5,3,0]
list2 = [9,4,6,9,5,3,2]

def greaterthan(list,num):
    for x in list:
      if x  num:      
        list.append(x)
    length = len(list)
    print 'Greater than',num,':',list
    print 'Count : ',length
    

greaterthan(list1,3)
     
      
        
        
        
        
        