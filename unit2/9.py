# lambda anonymous sunction to find bigger number in two given number
max = lambda x,y: x if x>y else y
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))

print("bigger number is:",max(a,b))