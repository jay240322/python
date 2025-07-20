# write a program to find out and display the common and the non common elements in 
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

for item in list1:
    if item in list2:
        print(item,"common element")
    else:
        print(item,"non common element")
# for item in list1:
#     if item not in list2:
#         print(item,"are not in element")
