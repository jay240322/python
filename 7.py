# access the base class constructor and method in a sub class key using super()
class square:
    def __init__(self,x):
        self.x = x

    def area(self):
        print("Area of square:",self.x*self.x)

class rectangle(square):
    def __init__(self, x,y):
        super().__init__(x)
        self.y = y

    def area(self):
        super().area()
        print("area of cube:",self.x * self.y)

length = int(input("enter the length of square:"))
breadth = int(input("enter the breadth of cube:"))
r = rectangle(length,breadth)
r.area()