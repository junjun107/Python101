# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Create a class
class User:
  #Constructor
  def __init__(self, name, age, email): #self = this (ES6)
    self.name = name
    self.age = age
    self.email = email

  def greeting(self):
    return f'My name is {self.name} and age is {self.age}'
  
  def has_birthday(self):
    self.age +=1

#Extend a class
class Customer(User):
  #constructor
  def __init__(self, name, age, email):
    self.name = name
    self.age = age
    self.email = email
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance
  def greeting(self):
    return f'My name is {self.name} and age is {self.age}. My balance is {self.balance}'

#Initialize User object
june = User('June Zhao', 37, 'junezhao@gmail.com')

#Initialize customer object 
janet  = Customer('Janet Smith', 45, 'janetS@gmail.com')

janet.set_balance(500)
print(janet.greeting())
# print(june.greeting())

june.has_birthday()  #run +1 to age first
# print(june.greeting()) 