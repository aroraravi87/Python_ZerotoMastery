def output(func):
    func()

def hello():
    print("Hello method called")

#Assign hello method to display variable.
display = hello

#delete the hello method
del hello

#output(display)

#############################
#Higher order function.(HOC)

#filter #reduce #map is higher order function becuase they accept function as parameters

def outputNew(func):
    func()

def sum():
    def func():
        return 10
    return func

#outputNew(sum)

########################
#custom decorator

def custom_decorator(func):
    def wrapper():
        print("\n#################")
        func()
        print("#################")
    return wrapper

@custom_decorator
def methodcall_withdecorator():
    print("Hello method called using custom decorator.")

def methodcall_withoutdecorator():
    print("\nHello method called without using custom decorator.")
    
#method calling 
methodcall_withdecorator()

methodcall_withoutdecorator()

#method calling
custom_decorator(methodcall_withoutdecorator)()


# custom decorator with parameter.

def custom_param_decorator(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper

@custom_param_decorator
def methodcall_withparam(message,emoji):
    print(message,emoji)

#method called with parameterized decorator
methodcall_withparam('Hello Mr.', ':)')
methodcall_withparam('Hello Mrs.', ':(')


#example 1 to measure the performance of function 

from time import time

def performance(func):
    def wrapper(*args,**kwargs):
        t1=time()
        func(*args,**kwargs)
        t2 = time()
        
        print("##### Output of example-1 ######")
        print(f"Time taken by method {t2-t1} s")
    return wrapper

@performance  
def iterate_method():
    for i in range(0, 1000000):
        i*10/2

iterate_method()    
 
 #example 2 to send message if authenicated
user1 = {
    'name': 'XYZ',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args,**kwargs)
    return wrapper

@authenticated
def message_friends(user):
    print("##### Output of example-2 ######")
    print('Message has been sent')

message_friends(user1)