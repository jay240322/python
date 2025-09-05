# a rpogram to accept elements in the form of tuple and display it's minimum,maximum,sum and average

num = eval(input("enter the elements in ():"))
print(num)
sum = 0
n = len(num)
for i in range(n):
    sum += num[i]

print("sum of numbers:",sum)
print("minimum numbers:",sum/n)
print("maximum numbers:",max(num))
print("average of numbers:",min(num))