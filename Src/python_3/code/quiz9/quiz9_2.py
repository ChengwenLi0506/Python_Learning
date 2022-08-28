
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# 消除警告信息
import warnings
warnings.filterwarnings(action="ignore")

#支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


# 从文件中读取数据
df = pd.read_csv('../../data/house.csv')
print(df)


# 第一张图，只考虑编号和价格
# 准备数据
x=df['row_id']
y=df['price']

#绘制图形
fig, ax = plt.subplots()

ax.scatter(x, y, s=150,c='r')
ax.plot(x,y)

plt.xlabel('编号')
plt.ylabel('价格')

plt.show()


# 第二张图，只考虑面积和价格
# 准备数据
x=df['area']
y=df['price']

#绘制图形
fig, ax = plt.subplots()

ax.scatter(x, y, s=150,c='b')
ax.plot(x,y)

plt.xlabel('面积')
plt.ylabel('价格')

plt.show()


