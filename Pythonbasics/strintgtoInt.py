def method1():
    str_numbers=['1','2','3','4','5']
    int_numbers=[]
    
    for item in str_numbers:
        int_numbers.append(int(item))
        
    print(int_numbers)
    
def method2():
    str_numbers=['1','2','3','4','5']
    
    int_numbers=[int(x) for x in str_numbers]
        
    print(int_numbers)

def method3():
    str_numbers=['1','2','3','4','5']
    
    int_numbers=list(map(int,str_numbers))
        
    print(int_numbers)

        
method1()
method2()
method3()