



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

# DataFrame中的值就旧 ndarray
print(type(df.values),'\n',df.values)

print('-'*100)

# 取DataFrame中的一列 ，就是Series
s=df['N']
print(type(s))
print(s)

print('-'*100)

s=df.iloc[1]
print(type(s),'\n',s)

print('-'*100)

#如果取二行或者二列呢？ 那就不是Series，仍是DataFrame
a=df.iloc[:,:2]
print(type(a),'\n',a)








