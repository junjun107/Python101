#write out all four math functions
# add four math functions into a dictionary as values, keys = "+","-","*","/"
# try multiply 4 * 8

# use recursion to solve this problem, also works with another while loop

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


calculator_dict = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}

def calculator():
  should_accumulate = True

  num1 = float(input("what is your 1st number?: "))

  while should_accumulate:

    for symbol in calculator_dict:
      print(symbol)

    math_operator = input("what is the operation?: " )

    num2 = float(input("what is your next number?: "))

    answer = calculator_dict[math_operator](num1, num2)

    print(f"{num1} {math_operator} {num2} = {answer}")

    choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation ")

    if choice == 'y' :
      num1 = answer
    else:
      should_accumulate = False
      print("\n" *20)
      calculator()

calculator()