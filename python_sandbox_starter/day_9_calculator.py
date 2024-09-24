def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    
    should_accumulate = True
    
    n1 = float(input("Enter first number: "))
    
    while should_accumulate:
        for key in operations:
            print(key)
    
        choice = input("Enter a math operation from above: ")
        n2 = float(input("Enter second number: "))
    
        result = operations[choice](n1, n2)
        print(f"{n1} {choice} {n2} is {result}")
    
        # Ask if user wants to continue working with previous number
        should_continue = input(
            f"Enter 'y' to continue wokring with previous number {result} or enter 'n' to start a new calculation "
        )
    
        if should_continue == "y":
            n1 = result
        else: 
            should_accumulate = False
            print("\n" *40)
            calculator()

calculator()
# if continue, get user symbol choice, do math. basicallly start all over again. sooooooo use a while loop
# start a variable called should_accumulate, place at top
# if user don't want to continue, set should_accumulate to False
# start over again : method 1: put everything inside a while loop
# method 2: put everything inside a function, call the function inside itself -> the else part. RECURSION

