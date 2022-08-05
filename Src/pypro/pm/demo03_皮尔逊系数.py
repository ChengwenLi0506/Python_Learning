# 传统数据分析    VS      人工智能区别
#   count()            超参数(公式参数)
# 协方差:

x = [1.1,1.9,3]  # list
y = [5.0,10.4,14.6]

ex = (1.1 + 1.9 + 3) / 3
ey = (5.0 + 10.4 + 14.6) / 3
exy = (1.1*5.0 +1.9*10.4 + 3*14.6) / 3
con_x_y = exy - ex*ey
# 协方差
print(con_x_y)
# list 存储, narray计算
import numpy as np
x = np.array(x)
# 求x 方差 --》 开根号标准差
res = np.sqrt(np.mean((x - x.mean())**2))
print('x的标准差为:',res)
print('x的标准差为:',np.std(x))
# 皮尔逊系数
print(con_x_y / (np.std(x) * np.std(y)))
# 官方的皮尔逊系数
from scipy.stats import pearsonr
corr = pearsonr(x,y)
print(corr[0])