# Exercise 1: write a program which repeately reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers. if the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number. 

num = 0
tot = 0.0

while True: #begin a loop
  sval = input('Enter a number: ')
  if sval == 'done':
    break #exit conditon 
  try: #input sanity checking
    fval = float(sval) 
  except: #catch 
    print('Invalid input')
    continue #go back to the top
  # print(fval)
  num = num + 1
  tot = tot + fval

print('All Done, total is: ')
print(tot,num, tot/num)