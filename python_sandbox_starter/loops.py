# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people =['John', 'Paul', 'Sara', "Susan"]

#for loop
# for person in people:
#   print(f'current person is {person}')

# break a loop

# for person in people:
#   if person == 'Sara':
#    break
#   print(f'current person is {person}')
# current person is John
# current person is Paul. Loop stopped at Sara, so no susan 

#continue 
# for person in people:
#   if person == 'Sara':
#    continue
#   print({person}) 
# {'John'}
# {'Paul'}
# {'Susan'}


#range
# for i in range(len(people)):
#   print(people[i])

# for i in range(0,11):
#   print(i)
# While loops execute a set of statements as long as a condition is true.
count = 0
while count < 10:
  print(count)
  count+= 1