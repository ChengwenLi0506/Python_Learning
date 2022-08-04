import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")


# # 1, load the data from the file
# movies = pd.read_excel("../data/电影.xlsx")
# score = pd.read_excel("../data/评分.xlsx")
# print('-'*100)
#
# # 2, show the data basic info
# print(movies.info())
# print(score.info())
# print('-'*100)
#
# # 3, show the first 5 records of data
# print(movies.head(n=5))
# print(score.head(n=5))
#
#
#
# # 4, merge the data from the parts
# df = pd.merge(movies,score,on='电影编号',how="inner")
# df.to_excel('../data/电影推荐系统.xlsx',index=False)

# 从电影推荐系统.xlsx读取数据
df = pd.read_excel('../data/电影推荐系统.xlsx')

# 5, show the merge data info and the first 5 records
print('-'*100)
print(df.info())
print(df.head(n=5))

# # 6, show bar to review the data range
# import matplotlib.pyplot as plt
# # df['评分'].hist(bins=20)
# # # plt.show()

# # 7, need to check every movie's score
# 算平均分数
rattings = pd.DataFrame(df.groupby('名称')['评分'].mean())

# 按照评分排序
rattings = rattings.sort_values('评分',ascending=False)
print('-'*100)
print(rattings.info())
print(rattings.head(n=5))


print('-'*100)
# # 8, to avoid fake score, we still need get the count of score

# 添加评分次数列并给出次数
print(rattings)
rattings['评分次数'] = df.groupby('名称')['评分'].count()

print(rattings.head(n=5))
print('-'*100)

# rattings['评分次数'] = tmp #df.groupby('名称')['评分'].count()
# 按照评分次数排列
rattings = rattings.sort_values('评分次数',ascending=False)
print(rattings)
print('-'*100)

# rattings.to_excel('../data/排序.xlsx')

# 只取次数大于100的电影
rattings = rattings[rattings['评分次数']>100]
# rattings.to_excel('../data/排序_2.xlsx')
print(rattings)


print('-'*100)

#电影有9687部，用户有610人

# 创建透视图，以编号为索引，电影名称为列，内容为评分
user_movie = df.pivot_table(index='用户编号',columns='名称',values='评分')
print(user_movie)

print('-'*100)
print(user_movie.describe())

print('-'*100)

# 取出勇敢者的游戏（1995）那一列，默认为series
FG = user_movie['勇敢者的游戏（1995）']
# FG is  Series
# print(type(FG))
# print(FG)

print(pd.DataFrame(FG).head(n=5))

# # 利用前面讲到的corrwidh 函数计算 (阿甘正传)与其它电影的皮尔逊系数
# corr()是计算整张表的相关性
# corrwith(A)是计算整张表中其它物品和A物品之间的相关性
corr_FG = user_movie.corrwith(FG)
corr_FG.name = '相关系数'
print(corr_FG)
print('-'*100)



similarity = pd.DataFrame(corr_FG,columns=['相关系数'])
# # 如果某部电影评分用户评价勇敢者的游戏用户一个交叉项也没有,则就无法计算协方差,形成空值
print(similarity)



print('-'*100)
# # 可以通过dropna删除控制
similarity.dropna(inplace=True)
print(similarity)

print('-'*100)

# 把勇敢者的游戏和其他电影的系数与之前表格中的评分次数合并
similarity = pd.merge(corr_FG,rattings['评分次数'],left_index=True,right_index=True)
print(similarity)

similarity.to_excel('../data/相关系数.xlsx')

print('-'*100)
# 按照相关系数进行排列
similarity_new = similarity.sort_values(by='相关系数',ascending=False)
print(similarity_new)

print(similarity_new.head(n=10))

similarity_new.to_excel('../data/电影推荐.xlsx')



