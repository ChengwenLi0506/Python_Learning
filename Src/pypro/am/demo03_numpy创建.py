# 创建ndarray两种方式
import numpy as np  # ctrl + 鼠标单击查询源码
# 数据库记录 => 样本   字段 => 特征
import sys
for path in sys.path:
    print(path)

t1 = [1,2,3,4,1]
print(t1,type(t1))

t1 = np.arange(12)  # ndarray 矩阵
print(t1,type(t1),t1.shape)
# print(t1-t1)
# list 用于数据存储, narray用于科学计算
t1 = t1.reshape(3,4)  # 三个样本四个特征
print(t1,type(t1))

# 第二种方式 (np.array 支持把object转化ndarray)
t1 = np.array([['A',12,True],
          ['B',14,False]])
print(t1,type(t1),t1.shape)
