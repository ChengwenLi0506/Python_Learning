
import numpy as np
import pandas as pd

# 消除警告信息
import warnings
warnings.filterwarnings(action="ignore")


# 获取数据
df = pd.read_excel('../../data/mobile.xls')

# 查看数据
print(df.info())
print(df)

print('-'*100)

# 由于基站编号与分析无关，但是基站编号是此数据与其它数据进行关联的关键字段
# 所以不能去掉drop，故我们可以将它设置为索引
df = pd.read_excel('../../data/mobile.xls',index_col='基站编号')

# 查看数据
print(df.info())
print(df)

print('-'*100)

# 对数据进行归一化
# from sklearn.preprocessing import MinMaxScaler
#
# # 此方式会吧dataFrame转化为ndarray类型
# mm = MinMaxScaler(feature_range=(0, 1))
# data = mm.fit_transform(df)

# 如果不想改变类型,这建议手动运算
data:pd.DataFrame = (df - df.min()) / (df.max() - df.min())

print('归一化后的数据： ')
print(data, type(data))

print('-'*100)

# 利用K-means算法对数据进行聚类
from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)    # 根据题目要求，聚成3类
model.fit(data)                 # 训练模型

# 对于K-mean而言,训练的过程就是找特征质心的过程
# 有几个特征，就对应的有几个质心，此处是4个特征，所以有4个质心
# 要聚成几类，就对应的有几行，此处是3类，所以有3行
# 质心就是 3x4 的矩阵
print(model.cluster_centers_)


# 然后将类别写入原来的数据
# DataFrame本质是个dict结构,因此可以通过dict方式添加列
df['商圈类别'] = model.labels_

# 最后将数据保存下来，以便后续的可视化
df.to_excel("../../data/mobile2.xls")


