



import numpy as np
import pandas as pd

# ndarray
v=np.arange(16).reshape(4,4)
print(type(v),'\n',v)
print('-'*100)

# DataFrame
df=pd.DataFrame(data=v, index=list('abcd'),columns=list('MNOP'))
print(type(df),'\n',df)
print('-'*100)


#下面我们演示对ndarray的数据进行切片
#1, 取一个元素
a=v[1,2]
print(type(a))
print(a)
print('-'*100)

#2, 连续的行或连续的列
a=v[:2]
print(type(a))
print(a)
print('-'*100)

a=v[:,0:2]
print(type(a))
print(a)
print('-'*100)

a=v[:2,0:2]
print(type(a))
print(a)
print('-'*100)

#3, 连续的行和不连续的列
a=v[:2,[0,2]]
print(type(a))
print(a)
print('-'*100)

#4, 不连续的行和连续的列
a=v[[0,3],0:2]
print(type(a))
print(a)
print('-'*100)



#5, 不连续的行和不连续的列
#这里要小心，我们先按习惯思维来看，打算取四个元素，但只取了二个元素
a=v[[0,2],[0,2]]
print(type(a))
print(a)
print('-'*100)

#要结合方法2和方法3
a=v[:,[0,2]]
a=a[[0,2],:]
print(type(a))
print(a)
print('-'*100)


