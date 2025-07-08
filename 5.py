# write a program to find out and display the common and the non common elements in 
# the list using numbership operators

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Find common elements
common = [x for x in list1 if x in list2]

# Find non-common elements
non_common = [x for x in list1 + list2 if (x not in list1) or (x not in list2)]

print("Common elements:", common)
print("Non-common elements:", non_common)
# the list using numbership operators