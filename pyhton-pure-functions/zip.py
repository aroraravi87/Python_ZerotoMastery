number_list = [1, 2, 3, 4, 5]
character_list = ['a', 'b', 'c', 'd', 'e', 'f']

#created tuple and zip.

tuple_list=(2,4,6,8,10,12,14,16)

print(f"original list", number_list)

# map with list function return list of object
print(f"Zip list", list(zip(character_list, number_list,tuple_list)))

# map with list function return list of object
print(f"character list after zip", character_list)

