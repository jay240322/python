import math

def area_of_circle():
    radius = float(input("enter radius of circle:"))
    area = math.pi*radius**2
    print(f"area of cicle:{area:.2f}")

def area_of_triangle():
    base = float(input("enter base of triangle:"))
    height = float(input("enter height of triangle:"))
    area = 0.5*base*height
    print(f"area of triangle:{area:.2f}")

def area_of_square():
    side = float(input("enter side of square:"))
    area = side ** 2
    print(f"area of square:{area:.2f}")

def simple_interest():
    p = float(input("enter principal amount:"))
    r = float(input("enter rate of interest:"))
    n = float(input("enter year of interest:"))
    interest = (p*r*n)/100
    print(f"si:{interest:.2f}")

def main():
    while True:
        print("\n menu")