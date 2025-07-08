# write a python program to swap two numbers without taking temporary variable
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)