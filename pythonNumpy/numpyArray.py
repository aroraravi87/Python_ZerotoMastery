import numpy as np
x=np.array([1,2,3])
print(x)

'''Create 2D array'''

y=np.array([[1,2,3],[4,5,6]])
print(y)

'''Create 3D array'''

z=np.array([[1,2],[3,4],[5,6]],dtype=float)
print(z)
z1=np.array([[1,2],[3,4],[5,6]],dtype=bool)
print(z1)
z2=np.array([[1,2],[3,4],[5,6]],dtype=complex)
print(z2)

'''Arrange function'''
print("##############")
a=np.arange(1,10,2)
print(a)

'''Reshape function'''
print("##############")
b=np.arange(1,11).reshape(5,2) 
print(b)

b1=np.arange(1,11).reshape(2,5) 
print(b1)

print("##############")
c=np.ones((3,4))
print(c)

c1=np.zeros((1,2))
print(c1)

d=np.linspace(-10,10,20)
print(d)

print("##############")
ran=np.random.random((3,4))
print(ran)

print("##############")
id=np.identity(3,dtype=int)
print(id)