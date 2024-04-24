# def greet_with_name(name):
#   print(f"Hello {name}")
  
# greet_with_name('June')

# Write your code below this line 👇
import math
def paint_calc(height,width,cover):
    num_of_cans=int(math.ceil((height * width)/cover))
    print(f"You'll need {num_of_cans} cans of paint.")


# Write your code above this line 👆
# Define a function called paint_calc() so the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



# Write your code below this line 👇
def prime_checker(number):
  if number/1==number and number/number == 1 and number%2 != 0 and number%3 != 0:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")   
# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)