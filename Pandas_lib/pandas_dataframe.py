
'''Two-dimensional, size-mutable, potentially heterogeneous tabular data.'''

import pandas as pd
import numpy as np

#class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)

# Data frame loading data from file.
df= pd.read_csv('pythonfileIO/sad.txt')
print(df.head())

##constructing data frame  from a dictionary 
raw={'col1':[0,1], 'col2':[2,3]}
df=pd.DataFrame(data=raw)
print(df)

print("Transpose Data Frame\n",df.T)

#constructing data frame  from a dictionary including series
data={'col1':[0,1,2,3], 'col2': pd.Series([2,3], index=[2,3])}
df=pd.DataFrame(data=data, index=[0,1,2,3])
print(df)
print(df.dtypes)

#Constructing DataFrame from a numpy ndarray that has labeled columns:

df=pd.DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=['a','b','c'])
print(df)

#Constructing DataFrame from a numpy ndarray that has labeled columns:
data=np.array([(1,2,3),(4,5,6),(7,8,9)],dtype=[("a","i4"),("b","i4"),("c","i4")])
df= pd.DataFrame(data,columns=['c','a','b'])
print(df)

#Constructing DataFrame from dataclass:

from dataclasses import make_dataclass
point=make_dataclass("Point",[("x",int),("y",int)])
df=pd.DataFrame([point(0,0),point(1,1),point(2,2)])
print('DataFrame from dataclass',df)

#Constructing DataFrame from Series/DataFrame:
series= pd.Series([1,2,3], index=["a","b","c"])
df=pd.DataFrame(data=series,index=["a","b"])
print('Constructing DataFrame from Series:',df)

series1= pd.DataFrame([1,2,3], index=["a","b","c"],columns=["x"])
df=pd.DataFrame(data=series1,index=["a","c"])
print('Constructing DataFrame from DataFrame for x axis:',df)

