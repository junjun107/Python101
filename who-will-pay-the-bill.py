import random

friends = ["alice", "fred", "David", "Emanuel","James"]

# 1st option 
print(random.choice(friends))

# 2nd option
print(friends[random.randint(0,len(friends))])
