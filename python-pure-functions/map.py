number_list = [1, 2, 3, 4, 5]
 
def multiply_by2(item):
    return item * 2

print(f"original list", number_list)
## map with list return object
print(map(multiply_by2, number_list))
# map with list function return list of object
print(f"changed list",list(map(multiply_by2,number_list)))