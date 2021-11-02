#This is a unnecessary edit
name = str(input("Please enter your name: "))
email = str(input("Please enter your email adress: "))
age = str(input("Please enter your age: "))

customer = {
    "name": name,
    "email": email,
    "age": age
}

print(f"Hello {customer['name']}, welcome aboard!")
f = open("customer.md", "a")
f.write(customer["name", "email", "age"])
f.write("\n")
f.close()
