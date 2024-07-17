# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules


import datetime

from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))

today = datetime.date.today()
