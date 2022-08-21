
import numpy as np
import pandas as pd


#准备数据
x = np.array(['1', '2', '3', '4', '5'])
y = np.array([3, 15, 9, 12, 4])


#matplotlib
import matplotlib.pyplot as plt

plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)  #调用matplotlib的函数来绘制

plt.grid(color = 'r', linestyle = '--', linewidth = 0.5)
plt.show()



#seaborn
import seaborn as sns

sns.lineplot(data=y)    #调用seaborn的函数来绘制

plt.grid(color = 'g', linestyle = '--', linewidth = 0.5)
plt.show()



#pyeharts
#最大的不同是采用类的方式，而不是函数

# import pyecharts.options as opts
# from pyecharts.faker import Faker
from pyecharts.charts import Line

c = (
    Line()
    .add_xaxis(x.tolist())
    .add_yaxis("Line Test", y.tolist())
    .render("../data/line_base.html")
)


# matplotlib，seaborn是函数参数的方式
# pyecharts面向对象的方式



