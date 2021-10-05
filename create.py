usr = eval(input("Please enter '1' to create a python file and append information in it: \n"
                 "Press Ctrl+C anytime to exit: \n\n"))

f = open("appending_vibe.py", "r")
print("This is the content of 'appending_vibe.py':\n ")
print(">>>")
print(f.read())
print(">>>")
print("Please enter a line of code:\n")
if usr == 1:
    while True:
        f = open("appending_vibe.py", "a")
        f.write(input("\n >>> "))
        f.write("\n")
        f.close()