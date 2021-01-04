#fibnocci series with generators

def fibnocci(number):
    a = 0
    b = 1
    for item in range(number):
        yield a
        temp = a
        a=b
        b = temp + b
        
for i in fibnocci(21):
    print(i)

#fibnocci series with list

def fibnocci1(number):
    a = 0
    b = 1
    result=[]
    for item in range(number):
        result.append(a)
        temp1 = a
        a=b
        b = temp1 + b
    return result
        
for i in fibnocci1(21):
    print(i)
        

     