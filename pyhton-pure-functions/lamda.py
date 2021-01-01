#map, filter,reduce,zip with lamda expression 

from functools import reduce

#syntax 
# lambda param:action(param)

# Map
number_list = [2,3, 4, 5, 6]

print(f"multiple by 2 list :", list(map(lambda item: item * 2, number_list)))

# filter

print(f"filter list with even one out :", list(filter(lambda item: item % 2 == 0, number_list)))

#reduce

print(f"sum of list with reduce function :", reduce(lambda com,item: com+item, number_list))

#square list

print(f"square of list :", list(map(lambda item: item **2, number_list)))

#list sorting [(0,2),(1,5),(2,7),(10,-1)]

list1 = [(0, 2), (1, 5), (2, 7), (10, -1)]

list1.sort(key=lambda x: x[0])

# sorting based on key.
print(f"sorting of list based on key:", list1)

#sorting based on value.

list1.sort(key=lambda x: x[1])

print(f"sorting of list based on value :", list1)
