# pass a list to a function or diplay it
def modify(list):
    list.append(4)
    print(list,id(list))

list = [1,2,3]
modify(list)
print(list,id(list))