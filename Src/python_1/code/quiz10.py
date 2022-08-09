
import numpy as np
import pandas as pd

data1={'name':['shan','shi','wu'],'age':[18,33,40]}
data2={'name':['shan','shi', 'liu'],'height':[185,173,157]}
a=pd.DataFrame(data=data1)
b=pd.DataFrame(data=data2)

print('table a: ')
print(a)

print('table b: ')
print(b)

print('-'*100)
in_=pd.merge(a, b, on='name', how='inner')
left_=pd.merge(a, b, on='name', how='left')
right_=pd.merge(a, b, on='name', how='right')

print('inner connect')
print(in_)

print('left connect')
print(left_)

print('right connect')
print(right_)

