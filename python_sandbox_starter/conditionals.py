def minimal_number_of_packages(items, available_large_packages, available_small_packages):
 #Fill 3 large boxes itmes /15 
# check remainder, items - items/15
  remaining_items = items
  large_capacity = 5
  small_capacity = 1
  large_box_needed = items// large_capacity
  remaining_items = items% large_capacity

  if remaining_items> available_large_packages:
     large_box_needed+= 1
     remaining_items -= available_small_packages
     available_small_packages = 0
  else:
     available_small_packages -= remaining_items

if __name__ == "__main__":
    print(minimal_number_of_packages(13, 3, 10))

  