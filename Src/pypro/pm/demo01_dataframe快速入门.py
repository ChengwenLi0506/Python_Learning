import pandas as pd  #
import numpy as np
# 手动构建Series (类首字母大写)
ss = pd.Series(data=['A','B','C','D'],name='type',index=list('abcd'))  # 创建Series对象
print(ss,type(ss))
# 手动构建DataFrame (二维)
val = np.arange(12).reshape(3,4)
df = pd.DataFrame(data=val,index=list('xyz'),columns=list('abcd'))
print(df,type(df))
# 三种方法获取行与列信息
ss = df["a"]  # 一般列操作,直接可以通过列名获取若干列
print(ss,type(ss))
# 通过索引 iloc 与ndarray语法相同 [行,列]
print(df.iloc[:,1:])
# 也可以通过名字 loc[行,列]
print(df.loc['x',['c','d']])
# Series DataFrame ndarray的关系
# 1: DataFrame 某一列(行),就是一维的Series
# 2: 无论是DF,Series 里面的数据都是ndarray类型
print(df.index,df.columns)
print(df.values,type(df.values))
# Dataframe 和 dict 是相互转化
val = {'p':['python','php'],'j':['java','js']}
df = pd.DataFrame(data=val,index=['a','b'])
# 列名就是dict key
print('-'*100)
print(df['p'])
print(val['p'])