number_list = [1, 2, 3, 4, 5]

new_number_list=number_list
 
def filter_odd_out(item):
    return item % 2!=0

print(f"original list", number_list)
## map with list return object
print(map(filter_odd_out, number_list))

# map with list function return list of object
print(f"filter list", list(map(filter_odd_out, number_list)))

# map with list function return list of object
print(f"current list", number_list)

print(f"filter odd list", list(filter(filter_odd_out, new_number_list)))

# map with list function return list of object
print(f"New list", new_number_list)