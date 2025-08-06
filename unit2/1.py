# Retrive,display,update only a range of elements from a array using indexing and sliceing in arrays
from array import *
x = array('i',[10,20,30,40,50,60,70])
n = len(x)
for i in range(n):
    print(x[i],end="  ")

print("\n updated array:")
x[2:5] = array('i',[4,5,6])
print(x)

print("\n sliced array:")
for i in x[2:6]:
    print(i,end="  ")