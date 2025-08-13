# write a program to create a list using range function and perform append,update and delete elements operations in it
list1 = list(range(10))
print("original list:",list1)

print(" ")

list1.append(int(input("enter the number to append:")))
print(f"list after appending:{list1}")

list1[1] = int(input("enter num for update the list at index 1:"))
print(f"list after updateing :{list1}")

list1.remove(int(input("enter num of list for delete:")))
print(f"list after deleting:{list1}")