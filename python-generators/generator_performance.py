#example to measure the performance of Generator or iterable.

from time import time

def performance(func):
    def wrapper(*args,**kwargs):
        t1=time()
        func(*args,**kwargs)
        t2 = time()

        print(f"Time taken by method {t2-t1} s")
    return wrapper

@performance  
def generator_performance():
    print('#Range') #Generator
    for i in range(100000000):
        i * 10

@performance  
def list_performance():
    print('#list') #List
    for i in list(range(100000000)):
        i * 10 


generator_performance()
list_performance()

 
