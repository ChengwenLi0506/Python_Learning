# 创建ndarray两种方式
import numpy as np  # ctrl + 鼠标单击查询源码
# 数据库记录 => 样本   字段 => 特征
import sys

t1 = np.arange(12)  # ndarray 矩阵
print(t1,type(t1),t1.shape)

print('-'*100)
t1 = t1.reshape(3,4)  # 三个样本四个特征
print(t1,type(t1),t1.shape)
t2=t1
# ndarray与某个数字运算
t = t2-5
print(t,type(t),t.shape)
# 比较运算 (数据的过滤)
t = t2>5
print(t,type(t),t.shape)

t = t2[t2>5]   #值的选择，只选择True对应的值，矩阵维度发生了变化
print(t,type(t),t.shape)

