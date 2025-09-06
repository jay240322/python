# a program to check the object type to know wheather the method exits in the object or not 

class dog:
    def bark(self):
        print("woww woww")

class duck:
    def talk(self):
        print("quack quack")

class human:
    def talk(self):
        print("hello")

def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()

    elif hasattr(obj,"talk"):
        obj.talk()

    else:
        print("sorry wrong object")

x = duck()
call_talk(x)
x = human()
call_talk(x)
x = dog()
call_talk(x)


