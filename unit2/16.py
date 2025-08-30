# create a dictionary that will accept cricket player name,score also we retrieving runs by entering the player's name

x = {}
print("how many players:")
n = int(input())

for i in range(n):
    print("enter player name:")
    k = input()
    print("enter runs:")
    v = int(input())
    x.update({k:v})

print(x)

print("enter players name for score detail:")
name = input()

runs = x.get(name,-1)
if(runs == -1):
    print("player not found")
else:
    print("{} made runs {}".format(name,runs))