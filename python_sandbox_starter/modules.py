# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#core modules
import datetime
import time

#pip module
from camelcase import CamelCase

#import custom modules created at validator.py (email checker module)
import validator
from validator import validate_email

today = datetime.date.today()
timestamp = datetime.time()

c = CamelCase()
print(c.hump('hello there world'))#convert a string into camel case format.

email = "test#example.com"
if validate_email(email):
  print('email is valid')
else: 
  print('email is not valid')

