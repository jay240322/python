# create a simple list with 7 elements and apply : append,insert,copy,remove,extend,count,pop,sort,reverse,clear

num = [10,20,30,40,50,60,70]
print(f"original list:{num}")
print(" ")
n = len(num)
print(f"number of elements in list:{n}")
print(" ")

num.append(80)
print(f"after appending 80 :{num}")
print(" ")

num.insert(1,99)
print(f"after inserting 99 at 1-posotion:{num}")
print(" ")

num1 = num.copy()
print(f"newly created copy list:{num1}")
print(" ")

num.append(50)
print(num)
n = num.count(50)
print(f"50 found {n} times")
print(" ")

num.remove(70)
print(f"after removing 70",num)
print(" ")

num.pop()
print('list after using pop()',num)
print(" ")

num.sort()
print(f"after using sort: {num}")
print(" ")

num.reverse()
print(f"after using reverse : {num}")
print(" ")

num.clear()
print(f"after using clear() : {num}")