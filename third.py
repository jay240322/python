# write a python program to create a byte type array,read,modify,and displaythe elements of the array
# Create a byte array
byte_arr = bytearray([10, 20, 30, 40, 50])

# Display original elements
print("Original array:", list(byte_arr))

# Read elements
for i, val in enumerate(byte_arr):
    print(f"Element at index {i}: {val}")

# Modify elements (e.g., increment each by 5)
for i in range(len(byte_arr)):
    byte_arr[i] += 5

# Display modified elements
print("Modified array:", list(byte_arr))