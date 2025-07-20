a = 25
b = 25
print(id(a))
print(id(b))

if(a is b):
    print("a and b have same identity")
else:
    print("a and b havenot same identity")