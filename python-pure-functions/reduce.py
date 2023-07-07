#Reduce function contains into below package.

from functools import reduce

number_list = [1, 2, 3, 4, 5,6,7,8,9,10]

def sumoflist(com, item):
    print(com,item)
    return com+item

print(f"original list", number_list)

# map with list function return list of object
print(f"Sum of list : ", reduce(sumoflist, number_list,0))



