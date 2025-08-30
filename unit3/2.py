# a program to demonstrate the use of instance and class/state variables

class sample:
    var = 10

    @classmethod
    def new_modify(cls):
        cls.var += 1

s1 = sample()
s2 = sample()

print("x in s1",s1.var)
print("x in s2",s2.var)

s1.new_modify()
print("x in s1",s1.var)
print("x in s2",s2.var)

print("")
print("using static method")

class sample:
    def __init__(self):
        self.x = 10
    
    def modify(self):
        self.x += 1

s1 = sample()
s2 = sample()

print("x in s1",s1.x)
print("x in s2",s2.x)

s1.modify()
print("x in s1",s1.x)
print("x in s2",s2.x)