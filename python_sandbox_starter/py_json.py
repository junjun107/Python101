# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

userJson = '{"first_name": "John", "last_name": "Smith", "age": 30}'

#Parse JSON to Dictionary
user = json.loads(userJson)

# print(user)
# print(user['first_name'])

#Turn Dictionary into JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year':1970}

carJSON = json.dumps(car)

print(carJSON)