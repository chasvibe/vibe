print("\n   ¤Hello, and welcome to this application designed to¤    ")
print("¤calculate the volume of equilateral cube and tetrahedron!¤\n")
print("You'll now be given two choices:")
print("1. Do you want to calculate the volume of a cube?")
print("2. Do you want to calculate the volume of a tetrahedron?\n")


def choice1():
    print("This is choice 1!")


def choice2():
    print("This is choice 2!")


while True:
    try:
        choice = eval(input("Press '1' or '2' to make a choice!"))
        if choice == 1:
            choice1()
        elif choice == 2:
            choice2()
    except NameError:
        print("Invalid input")

