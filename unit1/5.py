# write a program to find out and display the common and the non common elements in 
list1 = [10,20,30,40]
list2 = [40,50,60,10]

for item in list1:
    if item in list2:
        print(item,"is common element")
    else:
        print(item,"non common element")
# for item in list1:
#     if item not in list2:
#         print(item,"are not in element")
