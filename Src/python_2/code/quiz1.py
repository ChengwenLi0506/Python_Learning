
# 第一种导入模块的方式
print('第一种导入模块的方式')
# import 包.包...模块 as 别名

import numpy as np

data=np.arange(12).reshape(3,4)
print(type(data), '\n', data)


import pandas as pd

df=pd.DataFrame(data,index=list('xyz'),columns=list('ABCD'))
print(type(df), '\n', df)




# 第二种导入模块的方式
print('第二种导入模块的方式')
# from 包.包...模块 import 类或函数

from numpy import arange

data2=arange(16).reshape(4,4)
print(type(data2), '\n', data2)

from pandas import DataFrame

df2=DataFrame(data2,index=list('ijkl'),columns=list('EFGH'))
print(type(df2), '\n', df2)



