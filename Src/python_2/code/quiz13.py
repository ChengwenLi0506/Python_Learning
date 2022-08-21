

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from matplotlib import ticker

# 消除警告信息
import warnings
warnings.filterwarnings(action="ignore")


#支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


# default sheet_name = 0，表示第一张表，即2021年的月度汽车销量
df21 = pd.read_excel("../data/byd_sales.xlsx",names=['月份','2021'])
print(df21)

print('-'*100)

# sheet_name = 1，表示第二张表，即2022年的月度汽车销量
df22 = pd.read_excel("../data/byd_sales.xlsx",sheet_name=1,names=['月份','2022'])
print(df22)

print('-'*100)

# 2021年有12个月的销量，但是2022年只有7个月的销量
# 将二张的数据合并到一张表里，只取前7个月的数据，采用内连接的方式
df=pd.merge(df21, df22, 'inner')
print(df)

# bar的显示有二种方法
# 方法1，利用x和height传数据
# 方法2，利用data传数据，x和height只是这个数据中的二个特征
# 本演示采用第2种方法，所以先构建二个数据DataFrame

# 为了方便显示双柱状图， 我们将数据拆分成二张表
df_bar_1 = df.iloc[:, [0,1]]
df_bar_2 = df.iloc[:, [0,2]]

print('-'*100)
print(df_bar_1)
print(df_bar_2)



# 下面准备开始绘制图形

# 双坐标轴 （左边轴 和 右边轴）
fig, ax1 = plt.subplots()
# ax1 是左边轴

bar_width = 0.4  # 设置柱宽

# x 坐标轴的位置值分别为 [0, 1, 2, 3, 4, 5, 6]
# 类别1横坐标左移半个柱宽
df_bar_1['x_new'] = [i - bar_width / 2 for i in np.arange(len(df_bar_1['月份']))]

# 类别2横坐标右移半个柱宽
df_bar_2['x_new'] = [i + bar_width / 2 for i in np.arange(len(df_bar_2['月份']))]

print('-'*100)
print(df_bar_1)
print(df_bar_2)


# matplotlib的绘制图形部分
# 显示水平分隔线
ax1.grid(b="True",axis="y")

# 显示二根柱状态图，数据放在data里，x和height分别是数据中的二个特征
# edgecolor表示边框颜色
# linewidth表示边框线宽度
ax1.bar(x='x_new', height='2021', data=df_bar_1,width=bar_width,color="#90B3E3",edgecolor='white',linewidth=2)
ax1.bar(x='x_new', height='2022', data=df_bar_2,width=bar_width,edgecolor='white',linewidth=2)


# 纵坐标Y方向的刻度值，从0 到 180000
ax1.set(ylim=(0, 180000))

# 横坐标X方向的标识，就是月份值 （1月 到 7月）
plt.xticks(np.arange(len(df)), df['月份'])


# plt.xlabel('月份')
# plt.ylabel('销量')
plt.title('2021-2022年销量数据同比')

# ax1.legend(loc="upper left")

# 柱状图上方写文字
for x,y in enumerate(df_bar_1['2021']):
    ax1.text(x-bar_width/2,y+100,'%s'%y,ha='center',color='black')
for x,y in enumerate(df_bar_2['2022']):
    ax1.text(x+bar_width/2,y+100,'%s'%y,ha='center',color='black')


ax2 = ax1.twinx()
# ax2 是右边轴

# 绘制折线
# x坐标轴：[0, 1, 2, 3, 4, 5, 6]
df_x = [i for i in np.arange(len(df['月份']))]

# y坐标轴是计算出同比
df_y = []
for i in np.arange(len(df['月份'])):
    v = (df['2022'][i]-df['2021'][i])/(df['2021'][i])
    v = round(v, 3)     # 表示三位小数位
    df_y.append(v)

print(df_x)
print(df_y)

ax2.plot(df_x,df_y,color="#90B3E3",linewidth=3)
ax2.set(ylim=(0, 3.5))

# 下面设置表示y坐标轴按百分比来显示
ax2.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1,decimals=0))

# 折线图上写文字，注意format中%s，表示显示数值，%%表示显示百分比
for x,y in enumerate(df_y):
    ax2.text(x,y,'%s%%'%(100*y),ha='center',color='red')

plt.show()





