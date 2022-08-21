


import numpy as np
import pandas as pd

d = np.arange(12).reshape(3,4)
print(d, type(d))

v = d>5
print(v, type(v))

print('-'*100)

v=d[d>5]
print(v, type(v))

print('-'*100)





# from 包.包.模块 import 函数
from sklearn.datasets import load_iris

# from 包.包.模块 import 类
# 只有类的命名,采用驼峰命名法
from sklearn.utils import Bunch

df = load_iris()
print(type(df),'\n',df.keys())


T = df['data']  # 特征
y = df['target'] # 分类


# 150样本4个特征，前二个是萼片的长和宽，后二个是花瓣的长和宽
print(T,'\n',T.shape)
# 150样本类别值
print(y,'\n',y.shape)


print('-'*100)

X0 = T[y==0,0]
print(X0,'\n',X0.shape)

print('-'*100)

# X1 = T[y==1,0]
# X2 = T[y==2,0]





