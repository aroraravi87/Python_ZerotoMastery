import json

def custom_decorator(func):
    def wrapper():
        print("\n#################")
        func()
        print("#################")
    return wrapper

@custom_decorator
def dictionary():
    dic={
        "Name":"ABC",
        "Age":"20",
        "Address":"Can"
    }

    #print(dic.items())
    #print(dic.keys())
    #print(dic.values())

    for key in dic:
        print(f"key is {key} and value is {dic[key]}")
     
@custom_decorator   
#lamda expression
def lamda_method():
    my_list= range(16)
    result=filter(lambda x:x%3==0,my_list)
    for item in result:
        print(item)

    
#json view

@custom_decorator
def jsonformat():
    x='{ "Name":"ABC","Age":"20","Address":"Can"}'
    y=json.loads(x)
    print(y["Address"])

#methods calls.

dictionary()
lamda_method()
jsonformat()    