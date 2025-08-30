# write a python program to accept a student class with constructor having more than one perameter . also create a method named display() to view student details.

class student:
    def __init__(self,nm="",ag=15,m=0):
        self.name = nm
        self.age = ag
        self.marks = m

    def display(self):
        print("name",self.name)
        print("age",self.age)
        print("marks",self.marks)

s = student("nisha",18,46)
s.display()
s1 = student("sharma")
s1.display()