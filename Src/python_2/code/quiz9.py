
import numpy as np
import pandas as pd

d = np.arange(12).reshape(3,4)
print(d, type(d))

df = pd.DataFrame(data=d, index=list('ABC'), columns=['列一','列二','列三','列四'])
print(df, type(df))

print('-'*100)

# iloc中的i表示index，即是索引
#iloc [行，列]，如果是全部列，列可以省，但是行不能省
v = df.iloc[2,]
print(v, type(v))


v = df.iloc[:,2]
print(v, type(v))

print('-'*100)

# loc是直接用name
# loc [行，列]
v = df.loc['A',]
print(v, type(v))


v = df.loc[:,'列三']
print(v, type(v))

print('-'*100)


# 列是可以作为下标直接引用，但是行是不行的
# 这里需要展开数据的格式，一般行是样本，行是特征，数据分析主要是针对列的分析

v = df['列四']
print(v, type(v))

# v = df['A']
# print(v, type(v))

print('-'*100)


