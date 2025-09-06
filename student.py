# create a student class which have set_id,get_id,set_name,get_name,set_marks and set_marks,matched name starting with set are used toassign values and method name starting with get are returing the values,
# crate another file for use the student class which is already available in student.py

class student:
    def setid(self,id):
        self.id = id

    def getid(self):
        return self.id
    
    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name
    
    def setaddress(self,address):
        self.address = address

    def getaddress(self):
        return self.address
    
    def setmarks(self,marks):
        self.marks = marks

    def getmarks(self):
        return self.marks