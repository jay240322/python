class father:
    def height(self):
        print("height is 6 feet")

class mother:
    def complexion(self):
        print("complexion is fair")

class child(father,mother):
    pass

c = child()
print("child inherited qualities")
c.height()
c.complexion()