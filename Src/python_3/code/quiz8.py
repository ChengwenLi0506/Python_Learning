
import numpy as np

source = [[90, 2, 10, 40],
          [60, 4, 15, 45],
          [75, 3, 13, 46]]

# 归一化数据处理
from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler(feature_range=(0, 1))
data = mm.fit_transform(source)

source1 = np.array(source)

print(source1)
print(data)

print('-'*100)

# 标准化数据处理
from sklearn.preprocessing import StandardScaler

std = StandardScaler()
data = std.fit_transform(source)

# 原始数据每列的平均值
# print(std.mean_)

print(source1)
print(data)

# 从标准化返回到原始数据
# std.inverse_transform(data)

