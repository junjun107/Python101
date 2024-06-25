# 0
rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
# 1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
# 2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
random1 = random.randint(0,2)
random2 = random.randint(0,2)
print(random1, random2)
if random1 == 0 and random2 == 1:
  print(f"random2 won. {paper} beats {rock}")
elif random1 == 0 and random2 == 2:
    print(f"random1 won. {rock} beats {scissors}")
elif random1 == 1 and random2 == 0:
    print(f"random1 won. {paper} beats {rock}")
elif random1 == 1 and random2 == 2:
    print(f"random1 won. {rock} beats {scissors}")
elif random1 == 2 and random2 == 0:
    print(f"random2 won. {rock} beats {scissors}")
elif random1 == 2 and random2 == 1:
    print(f"random1 won. {scissors} beats {paper}")
else:
    print("even. try again")