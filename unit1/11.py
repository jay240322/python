# convert length to inch
l = int(input("enter the length(in cm's):"))

if(l > 0):
    inch = float((l*l)/2.54)
    print("length in inches:",inch)
else:
    print("invalid")