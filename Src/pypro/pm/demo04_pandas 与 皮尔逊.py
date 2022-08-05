import pandas as pd

df = pd.DataFrame(data = [[5,1,5],[4,2,2],[4,2,1]],columns=['用户1','用户2','用户3'],index=['物品A','物品B','物品C'])
print(df)  # 基于物品的协同过滤
df = df.T  # 置换矩阵
print(df)  # 基于用户的协同过滤

from scipy.stats import pearsonr
# (相关系数r,显著性p) p<0.05 才说明有相关性
# 在样本量足够大 > 1000 时p才有意义
print(pearsonr([5,1,5],[5,1,5]))
print(pearsonr([5,1,5],[4,2,2]))
print(pearsonr([5,1,5],[4,2,1]))
# 获取特征列的相关性默认: pearson
# corr可以计算正张表的皮尔逊相关系数
print(df.corr())
#
#      用户1  用户2  用户3
# 电影A    5    1    5
# 电影B    4    2    2
# 电影C    4    2    1

A = df['物品A']
# corrwith 求某个列与其它的相关性
corr_A = df.corrwith(A)
print(corr_A)