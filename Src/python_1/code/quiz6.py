
import numpy as np

#numpy用于科学计算，就是矩阵的运算
v1=np.arange(12).reshape(3,4)

print(type(v1), '\n', v1)
print('-'*100)

v1=v1+5
print(v1)
print('-'*100)


l = [2,3,4,5]
v2=np.array(l).reshape(1,4)
print(type(v2), '\n', v2)
print('-'*100)

#默认的是数量积
v3=v1*v2
print(type(v3), '\n', v3)

print('-'*100)


v2=v2.reshape(4,1)
print(type(v2), '\n', v2)
print('-'*100)


#3x4  *  4x1 = 3x1
#dot才是矩阵乘法
v3=v1.dot(v2)
print(type(v3), '\n', v3)

print('-'*100)




#pandas用于数据处理，包括数据的加载，分片，合并，清洗，保存等
import pandas as pd

df = pd.read_csv('../data/house.csv')

print(type(df), '\n', df)

df1 = df.iloc[:,[1,2]]
print(type(df1), '\n', df1)

df1.to_excel('../data/house1.xlsx',index=False)

print('-'*100)



