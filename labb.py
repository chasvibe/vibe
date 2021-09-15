#|\     /|\__   __/(  ___ \ (  ____ \
#| )   ( |   ) (   | (   ) )| (    \/
#| |   | |   | |   | (__/ / | (
#( (   ) )   | |   |  __ (  |  __)
# \ \_/ /    | |   | (  \ \ | (
#  \   /  ___) (___| )___) )| (____/\
#   \_/   \_______/|______/ (_______/
#Both the functions made in this script are almost identical,
#which is why I'm using the same variable (userinput) but with a '2' in 'tetra()'
#Importing math module for square rooting
import math

#Welcome message that gives the user instructions on how to continue
print("\n   ¤Hello, and welcome to this application designed to¤    ")
print("¤calculate the volume of equilateral cube and tetrahedron!¤\n")
print("             ¤You'll now be given two choices:¤")
print("    ¤1. Do you want to calculate the volume of a cube?¤")
print(" ¤2. Do you want to calculate the volume of a tetrahedron?¤\n")
print("           ¤You can press return any time to quit¤")


#Function to calculate user input with the formula V=a^3 (The volume of a cube)
#Also added a sort of tryparse loop so that the program
#don't crash if the user inputs anything other than numbers
def cube():
    while True:
        try:
            userinput = eval(input("\n     ¤Please give me the width of the cube sides in cm¤ \n"))
            volume = userinput ** 3
            print("\n                        ¤Thank you!¤")
            print("   ¤The volume of your cube is ", volume, " cubic centimeters¤\n")
            break
        except NameError:
            print("    ¤Please enter in numbers (Input example: 10, 14, 25)¤ ")


#A function to calculate user input with the formula: V=Square root of a^3/6 (The volume of a tetrahedron)
#Also added the tryparse here
def tetra():
    while True:
        try:
            userinput2 = eval(input("\n ¤Please give me the width of the tetrahedron's sides in cm¤ \n"))
            tetravolume = math.sqrt((userinput2 ** 3) / 6)
            print("\n                        ¤Thank you!¤")
            print("¤The volume of your tetrahedron is ", tetravolume, " cubic centimeters¤\n")
            break
        except NameError:
            print("    ¤Please enter in numbers (Input example: 10, 14, 25)¤ ")

#Tryparse to get the users first input (if they want to calculate the volume of the cube, or the tetrahedron)
while True:
    try:
        choice = eval(input("      ¤Press '1' or '2' then enter to make a choice!¤ \n"))
        if choice == 1:
            cube()
        elif choice == 2:
            tetra()
    except NameError:
        print("                       ¤Invalid input¤")
