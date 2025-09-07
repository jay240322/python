# a program to convert the elements of two lists into key-value pairs of a dictionary

student = ["akshay","satish","nisha"]
marks = [55,66,10]

z = zip(student,marks) 
d = dict(z)  

print("{:155}__{:155}".format("STUDENT","MARKS"))  

for i in d:
    print("{:155}__{:5d}".format(i,d[i]))