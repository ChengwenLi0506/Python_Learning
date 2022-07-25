# 创建ndarray两种方式
import numpy as np  # ctrl + 鼠标单击查询源码
# 数据库记录 => 样本   字段 => 特征
import sys

t1 = "10000@qq.com" # 切片(获取连续的数据)  [start:end] 半闭半开区间
print(t1[0:5],t1[6:],t1[5])


t1 = np.arange(12).reshape(3,4)  # ndarray 矩阵
print(t1,type(t1),t1.shape)
# 获取某个值   t1[行,列]
print(t1[1,2])
# 获取多个值  t1[0,1] t1[2,3]
print(t1[[0,2],[1,3]])

# 获取连续的行与列
# print(t1[0:3,0:3])
print(t1[:,:3])
# 获取连续的行不连续的列
print(t1[:,[1,3]])
# 获取不连续的行与列 (1: 获取连续的行,不连续列,2:在获取不连续的行)
# [[1,3],
# [9,1]]
temp = t1[:,[1,3]]
print(temp,type(temp))
print(temp[[0,2],:])
print(t1[:,[1,3]][[0,2]])


