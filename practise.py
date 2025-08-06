group1 = [1,2,3,4,5]
search = int(input("enter number to search:"))
for i in group1:
    if search == i:
        print("found",search)
        break
else:
    print("not found",search)