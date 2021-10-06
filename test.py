def my_function():
    pass


def my_second_function(surname, last_name):
    return f"Hello {surname} {last_name}!"


def my_math_function(num1, num2):
    return num1 * num2


while True:
    try:
        numb1 = eval(input("Please enter a number: "))
        numb2 = eval(input("Please enter one more: "))
        print(my_math_function(numb1, numb2))
    except TypeError:
        print("Please enter an integer: ")