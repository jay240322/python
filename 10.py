# understand the order of execution of python methods in several base,classes according to method resolution order(MRO)

class A(object):
    def method(self):
        print("method of class A")
        super().method()

class B(object):
    def method(self):
        print("method od class B")
        super().method()

class c(object):
    def method(self):
        print("c class method")

class x(A,B):
    def method(self):
        print("method of class x")
        super().method()

class y(A,B):
    def method(self):
        print("method of class y")
        super().method()

class p(x,y,c):
    def method(self):
        print("method of class p")
        super().method()

newp = p()
print(p.mro())
newp.method()