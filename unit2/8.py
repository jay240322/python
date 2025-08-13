# use of positional argument,keyword argument,default argument,variable length argument
print("positional argument")
def attach(s1,s2):
    s3 = s1 + s2
    print("total string:" +s3)
attach("hello","world")

print(" ")

print("keyword argument")
def find(item,price):
    print("item = %s" % item)
    print("price = %d" % price)
find(price=100,item="apple")
find(item="banana",price=200)

print(" ")

print("default argument")
def find(item,price = 40):
    print("item = %s" % item)
    print("price = %.2f " % price)
find(item = "banana")
find(item = "potato",price= 30)

print(" ")

# def adder(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print("sum = %d" % sum)
# adder(10,20,30)
