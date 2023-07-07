from time import time

def performanace(func):
    def wrapper(*args,**kwargs):
        t1=time()
        func(*args,**kwargs)
        t2=time()
        
        print ("##### Measure the performance ####")
        print (f"perofmance measurement {t2-t1} s")
    return wrapper
    

@performanace
def calculate_measure():
    list1= {num**2 for num in range(0,200) if num%2!=0}
    print(list1)
  
    
calculate_measure()
    
    
    
