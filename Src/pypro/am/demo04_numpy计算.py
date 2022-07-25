# 创建ndarray两种方式
import numpy as np  # ctrl + 鼠标单击查询源码
# 数据库记录 => 样本   字段 => 特征
import sys

t1 = np.arange(12)  # ndarray 矩阵
print(t1,type(t1),t1.shape)
t1 = t1.reshape(3,4)  # 三个样本四个特征
print(t1,type(t1))
t2 = t1
# 基本运算: 算数,比较
print(t2 - t1)  # 同维度,每个对应的值分别运算
# ndarray与某个数字运算
print(t2 - 5)
# 比较运算 (数据的过滤)
print(t2[t2 > 5])


