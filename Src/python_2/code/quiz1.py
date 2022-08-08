
import numpy as np

data=np.arange(12).reshape(3,4)
print(type(data), '\n', data)


import pandas as pd

df=pd.DataFrame(data,index=list('xyz'),columns=list('ABCD'))
print(type(df), '\n', df)


# from pandas import DataFrame
#
# df2=DataFrame(data,index=list('ijk'),columns=list('EFGH'))
# print(type(df2), '\n', df2)


