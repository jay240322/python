# a python function to accept python function as a dictionary and display it's elements 
def fun(dictionary):
    for i,j in dictionary.items():
        print(i,"--",j)

d = {"a":"apple","b":"banana","c":"carrot"}
fun(d)
