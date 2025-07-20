# # write a python program to create a byte type array,read,modify,and displaythe elements of the array
# # Create a byte array
# byte_arr = bytearray([10, 20, 30, 40, 50])

# # Display original elements
# print("Original array:", list(byte_arr))

# # Read elements
# for i, val in enumerate(byte_arr):
#     print(f"Element at index {i}: {val}")

# # Modify elements (increment each by 5)
# for i in range(len(byte_arr)):
#     byte_arr[i] += 5

# # Display modified elements
# print("Modified array:", list(byte_arr))
elements = [10,20,30,40]
print("the elements without modify:",elements)

x = bytearray(elements)
x[0] = 88
x[1] = 99

print("the elements after modify:")
for i in x:
    print(i)
