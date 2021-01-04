#List- iterable 
#range- generator.

# list is iterable but not generator but range is generatable not iterable.
#generator is the subset of iterable.

def list_object(num):
    result=[]
    for item in range(num):
         result.append(item * 2)
    return result

new_list = list_object(1000)
#print(new_list)


# create custom generator.

def generator_obj(num):
    for item in range(num):
        yield item * 2


gen_obj = generator_obj(10)
next(gen_obj)
next(gen_obj)
print(next(gen_obj))

print(next(gen_obj))