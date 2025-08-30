# sort a tuple with nested list 

emp = ((10,'ajay',4000),(20,'vijay',5000),(30,'jay',6000))

print(sorted(emp))
print(sorted(emp,reverse = True))
print("")
print("sorting with name")
print(sorted(emp,key=lambda x:x[1]))
print("")
print("sorting with salary")
print(sorted(emp,key=lambda x:x[2]))
