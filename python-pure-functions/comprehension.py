#list set dict with comprehension. 

#list comprehension

list1 = [num for num in [1, 2, 3, 4, 5]]
print(list1)
list1 = [num for num in range(0,50)]
print(f"Range volume :",list1)
list1 = [num*2 for num in range(0,50)]
print(f"Doubled volume :",list1)
list1 = [num for num in range(0,50) if num%2==0]
print(f"Filtered volume :", list1)

#Dict comprehension

dict1 = {
    'a':1,
    'b':2
}

list1 = {k:v*2 for k,v in dict1.items()}
print(list1)

list1 = {k:v**2 for k,v in dict1.items() if v%2==0}
print(list1)

list1 = {num:num*2 for num in [1,2,3,4,5]}
print(list1)

list1 = {num:num*3 for num in range(0,50) if(num%2!=0)}
print(list1)

#Set Comprehension

list1 = {num for num in range(0,50)}
print(f"Range volume :", list1)


list1 = {char for char in 'Hello'}
print(f"Set volume removed the duplicate one:", list1)

list1 = {num*2 for num in range(0,50)}
print(f"Doubled volume :",list1)

list1 = {num for num in range(0,50) if num%2==0}
print(f"Filtered volume :",list1)

#set comprehension to remove the duplicate from list.



sameple_list = ['a', 'b', 'c', 'c', 'd', 'e', 'f', 'f', 'n', 'a', 'b']

duplicates = []
for item in sameple_list:
    if sameple_list.count(item) > 1:
        if item not in duplicates:
            duplicates.append(item)

print(f"find duplicates by iteration",duplicates)


#find duplicate using set comprehension

list1=set([x for x in sameple_list if sameple_list.count(x)>1])
print(f"find duplicate by set comprehension",list(list1))

