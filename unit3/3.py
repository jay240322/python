# a program to store data into instance using mutator method and retieve data from the instances using accessor methods
class student:
    def setname(self,name):
        self.name = name
    def getname(self):
        return self.name
    def setmarks(self,marks):
        self.marks = marks
    def getmarks(self):
        return self.marks

n = int(input("how many students:"))
i = 0
while(i<n):
    s = student() 
    name = input("enter name :")
    s.setname(name)
    marks = int(input("enter marks:"))
    s.setmarks(marks)
    i += 1