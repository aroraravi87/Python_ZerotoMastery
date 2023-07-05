def my_gen():
    n=1
    print("This is first method")
    yield n
    
    n+=1
    print("This is second method")
    yield n
    
    n+=1
    print("This is last method")
    yield n
    
    
for item in my_gen():
    print(item)
