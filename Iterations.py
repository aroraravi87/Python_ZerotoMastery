## for loop
counter_list=[1,2,3,4,5,6,7,8,9,10]
sub_counter_list=['a','b','c','d','e','f','g','h','i','j']

for item in counter_list:
	for subitem in sub_counter_list:
		print(item,subitem)


user_details={
'Name':'ABC',
'Age':30,
'Married':True
}

# #iterable through for loop
for item in user_details:
	print(item)

print('############');

for item in user_details.keys():
	print(item)

for item in user_details.items():
	print(item)

for item in user_details.values():
	print(item)

for key,value in user_details.items():
	print(f"Key is {key} and value is {value}")

# #Sum of list item
count_item=[1,2,3,4,5]
sumitem=0
for item in count_item:
	sumitem+=item;
print(sumitem);

#Range function
for item in range(1,100,2):
	print(item)

#enumerate function
for index,char in enumerate(range(1,100,2)):
	if(char==61):
		print(index,char);

#while loop
counter=0
while counter<=50:
	print(counter)
	counter+=1
else:
	print('while completed')


#Walrus Operator :=
value='Welcome User'

if((newvalue :=len(value))>0):
	print(f"charcters lenght is {newvalue}")

while((newvalue :=len(value))>0):
	print(newvalue);
	value=value[:-1]