# a program to create static method that count the number of instances created for a class


class myclass:
    n = 0

    def __init__(self):
        myclass.n += 1

    @staticmethod
    def no_of_objects():
        print("no of instances created:", myclass.n)

obj1 = myclass()
obj2 = myclass()
obj3 = myclass()
obj4 = myclass()
myclass.no_of_objects()
