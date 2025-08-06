# search the position of the array from array using index() method of array class

from array import *
x = array('i',[])

print("how many element you want:")
n = int(input())

for i in range(n):
    print("enter the element:",end="")
    x.append(int(input()))
print("original array",x)

print("enter the element to search:")

s = int(input())

try:
    pos = x.index(s)
    print(f"found at {pos+1} position")

except ValueError:
    print("noe found")