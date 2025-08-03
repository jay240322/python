import math

def area_of_circle():
    radius = float(input("enter the radius of circle:"))
    area = math.pi*radius**2
    print(f"area of circle{area:.2f}")

def area_of_triangle():
    base = float(input("enter the base of triangle:"))
    height = float(input("enter the height of triangle:"))
    area = 0.5*base*height
    print(f"area of the triangle:{area:.2f}")

def area_of_square():
    side = float(input("enter side of the square:"))
    area = side ** 2
    print(f"area of square is:{area:.2f}")

def simple_interest():
    p = float(input("enter the princiapal of interest:"))
    r = float(input("enter the rate of the interest:"))
    n = float(input("enter the year for interest:"))
    interest = (p*r*n)/100
    print(f"simple interest:{interest:.2f}")

def main():
    while True:
        print("\n Menu")
        print("1. find the area of circle")
        print("2. find the area of triangle")
        print("3. find the area of square")
        print("4. find the simple interest")
        print("5. Exit")

        choice = int(input("enter the choice between(1-5):"))

        match choice:
            case 1:
                area_of_circle()

            case 2:
                area_of_square()

            case 3:
                area_of_square()

            case 4:
                simple_interest()

            case 5:
                print("exit the program")
                break

            case _:
                print("invalid chodie")

if __name__== "__main__":
    main()
