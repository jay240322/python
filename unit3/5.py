# create a bank class with two variables name and balance,implement a constructor to initialise the varaible . also implement deposit and withdrawl using instance methods

import sys
class bank(object):
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdrawl(self,amount):
        if amount > self.balance:
            print("low balance , can't withdrawl")

        else:
            self.balance -= amount

        return self.balance
    
name = input("enter name :")
balance = float(input("enter initial balance: "))
b = bank(name, balance)

while(True):
    print("d/D-deposit , W/w-withdraw , e/E - exit")
    choice = input("enter the choice :")

    if choice == 'e' or choice == 'E':
        sys.exit() 

    amount = float(input("enter the amount:"))

    if choice == "d" or choice == "D":
        print("balance after deposit:",b.deposit(amount))

    elif choice == "w" or choice == "W":
        print("balance after withdrawl:",b.withdrawl(amount))       