import numpy as np
obj=[1,2,3]
arr=np.array(obj)
print(arr)
arr=np.array(obj,dtype=complex)
print(arr)
arr=np.array(np.mat(obj))
print(arr)
## display multidimensional array.
arr=np.array(np.mat(obj),subok=True)
print(arr)

#concatenate funcion

x=np.array([[1,2],[3,4]])
y=np.array([[10,20]])
result= np.concatenate((x,y),axis=0)
print("concatenate\n", result)
result= np.concatenate((x,y.T),axis=1)
print("concatenate\n", result)
result= np.concatenate((x,y),axis=None)
print("concatenate\n", result)

## Masking with Arrange function
print('Masking with Arrange function')
x=np.ma.arange(5)
y=np.arange(3,7)
x[1]=np.ma.masked
print(x)
print(y)

x1=np.concatenate([x,y])
x2=np.ma.concatenate([x,y])
print(x1)
print(x2)

## ReShape Function

print('Reshaping Function')
x=np.arange(4)
y=np.reshape(x,(4,1))
print(x)
print(y)
