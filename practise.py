from array import *

array = array('i',[10,20,30,40,50])
print("original array:",array)

array.append(60)
print("after appending 60:",array)

array.insert(1,99)
print("after inserting 99 :",array)

array.remove(20)
print("after removing 20",array)

n = array.pop()
print("after poping the element:",array)
print("poped element:",n)

n = array.index(20)
print("the index of 30 is:",n)

lst = array.tolist()
print("list:",lst)
print("array:",array)

