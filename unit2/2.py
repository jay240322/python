# to understand various method of array class mentioned "append, insert, remove, pop, index, tolist and count"

from array import *

arr = array('i',[10,20,30,40,50])
print(f"original array:{arr}")

arr.append(60)
print(f"after appending: {arr}")

arr.insert(1,99)
print(f"after inserting: {arr}")

arr.remove(20)
print(f"aftr removing: {arr}")

n = arr.pop()
print(f"after poping: {arr}")
print(f"poped element:{n}")

n = arr.index(30)
print(f"index of 30 at: {n} position")

lst = arr.tolist()
print("list: ",lst)
print("array:",arr)