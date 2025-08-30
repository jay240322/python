# a program to use class method to handle the common features of all the instance of student class

class student:
    marks = 10

    @classmethod
    def modify(cls,name):
        print("{}scored{}marks".format(name,cls.marks))

student.modify("sanjay--")
student.modify("ajay--")


