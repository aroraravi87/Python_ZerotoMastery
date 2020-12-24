#custom functions default

def my_demo_func():
	print("demo function called");

my_demo_func()

#custom functions parametrized

def sum(n1,n2):
	return n1+n2;

print(sum(10,20))

# keyword parameterized

def user_Detail(name,age):
	print(f"Name of person is {name},age is {age}");

user_Detail('rosinger',30)
user_Detail('James',40)
user_Detail('Alien',50)

## keyword argument specified
user_Detail(age=20,name='sam')

def user_Detail_defualt(age,name='test_default'):
	print(f"Name of person is {name},age is {age}");

user_Detail_defualt(30)

#*args v/s **kwargs

def get_list(*args,**kwargs):
	print(args)
	print(kwargs)
	total=0
	for items in kwargs.values():
		total+=items
	print(sum(args)+total)

#keyword args num1=10,num=3
get_list(1,2,3,4,5,num1=10,num=30)

#rule param,args,default parametes,kwargs

get_list(10,1,2,3,dnum=100,n1=40,n2=50)

#get max from odd number

def is_odd(list):
	odds=[]
	for item in list:
		if item%2!=0:
			odds.append(item)
			continue
	print(max(odds))	


is_odd(range(1,30))


# docstring (method defination)

def printName(name):
	'''
	Print Method used to print the name of person.
	'''
	print(f"This method will print your name like {name}")

printName("ABC")


#Rules
# start with local
# local not exist then pick parent.
# look for global scope
# built in function scope

total=100 #global scope

def parent():
	total=50
	def child():
		#total=10
		return total
	return child()

#check built in function
def parent_fun():
	def child():
		return sum
	return child()


print(total)
print(parent())
print(parent_fun())

#Access Global variable within function. 

total=0

def calculate_Sum():
	global total
	total+=2
	return total

print(calculate_Sum())
print(calculate_Sum())
print(calculate_Sum())


#Access nonlocal variable in local scope and modify the Value
def outer():
	'''
 Access nonlocal variable in local scope and modify the Value.
	'''
	val=100
	def inner():
		nonlocal val
		val=150
		print(f"inner value is {val}")


	inner()
	print(f"outer value is {val}")

outer()



