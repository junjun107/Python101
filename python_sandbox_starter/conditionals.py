# If/ Else conditions are used to decide to do something based on something being true or false
# x= 10
# y = 10


# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

#if 
# if x > y:
#   print(f'{x} is greater than {y}')

# Logical operators (and, or, not) - Used to combine conditional statements

#if/else
# if x>y:
#   print(f'{x} is greater than {y}')
# else:
#   print(f'{y} is greater than {x}')

#elif
## if -> else if -> else 
# if x>y:
#   print(f'{x} is greater than {y}')
# elif x<y:
#   print(f'{y} is greater than {x}')
# else:
#   print("two numbers are the same")

  
# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object



# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
 # and 
 # or 
# not 

height = int(input("what's your height in cm?"))
if height >= 120:
  
  print("You can get on the ride")
  age = int(input("how old are you?"))
  if age > 18:
    print("Please pay $12")
  elif age >12 and age < 18:
    print("Please pay 7") 
  else:
    print("Please pay $5") 
else:
  print("Sorry you cannot get on the ride")