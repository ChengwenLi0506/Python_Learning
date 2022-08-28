
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston

# 消除警告信息
import warnings
warnings.filterwarnings(action="ignore")

#支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 数据的加载
lb = load_boston(return_X_y=False)

# 数据类型是一个sklearn中的一个类Bunch
# print(type(lb))
# print(lb)
# Bunch本质上就是一个字黄，所以我们可以通过Key来取数据

# 表示一共有506个样本，其中有13个特征
feature = lb['feature_names']
print('本数据一共有{n}个特征'.format(n = len(feature)))
print(feature)
print('-'*100)

X = lb['data']     # 506 x 13
y = lb['target']   # 506 x 1

print(X)
print(y)

#X.shape = (506, 13)  shape[0] = 506   shape[1] = 13
print(X.shape)
print(y.shape)

columns = X.shape[1]
colors = ['r','g','b','c','m','y','k']


#绘制图形
for i in range(columns):
    # print(i)
    # print(i%7)

    x = X[:,i]

    fig, ax = plt.subplots()
    ax.scatter(x, y, c=colors[i%7])
    plt.xlabel('特征: ' + feature[i])
    plt.show()


