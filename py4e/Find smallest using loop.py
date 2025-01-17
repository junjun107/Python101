# To find the smallest without knowing the data, the idea way to is to set smallest as the 1st element. so we set smallest to None, as a marker
smallest = None

for i in [11,2,13,24,35,46,27,18,19]:
    if smallest is None:
        smallest = i 
        # in first loop, it's the first element
    elif i < smallest:
        smallest = i;
        print(smallest, i)
print ("done", smallest )
