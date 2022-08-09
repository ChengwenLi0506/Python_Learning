import numpy as np
import pandas as pd

import warnings
warnings.filterwarnings("ignore")


# 1, load the data from the file
# 从二个文件中读取数据
movies = pd.read_excel("../data/电影.xlsx")
score = pd.read_excel("../data/评分.xlsx")
print('-'*100)

# 2, show the data basic info
print(movies.info())
print(score.info())
print('-'*100)

# 3, show the first 5 records of data
print(movies.head(n=5))
print(score.head(n=5))



# 4, merge the data from the parts
# 将二张表合并成一张表，由于它们有共同的字段 '电影编号'，采用内连接的方式
df = pd.merge(movies,score,on='电影编号',how="inner")
# 然后再把合并后的数据保存下来，不保留索引
df.to_excel('../data/电影推荐系统.xlsx',index=False)

# 5, show the merge data info and the first 5 records
print('-'*100)
print('经过合并后的数据： ')
print(df.info())
print(df.head(n=5))


# 从电影推荐系统.xlsx读取数据
# 重新读取数据，其实这一步的操作有点多余的
df = pd.read_excel('../data/电影推荐系统.xlsx')

# 5, show the merge data info and the first 5 records
print('-'*100)
print('经保存后再读取的数据： ')
print(df.info())
print(df.head(n=5))




# # 6, show bar to review the data range
# import matplotlib.pyplot as plt
# # df['评分'].hist(bins=20)
# # # plt.show()

print()
print('下列才是真正数据分析部分')
# # 7, need to check every movie's score
# 算平均分数
# groupby 相当于将名称作为索引产生一个新的DataFrame


rattings = pd.DataFrame(df.groupby('名称')['评分'].mean())
print('-'*100)
print(rattings.info())
print(rattings.head(n=5))

# 按照评分排序
# rattings = rattings.sort_values('评分',ascending=False)
# print('-'*100)
# print(rattings.info())
# print(rattings.head(n=5))


print('-'*100)
# # 8, to avoid fake score, we still need get the count of score

# 新添加一列评分次数，并调用count()计算出次数
rattings['评分次数'] = df.groupby('名称')['评分'].count()

print(rattings.head(n=5))
print('-'*100)

# rattings['评分次数'] = tmp #df.groupby('名称')['评分'].count()
# 按照评分次数排列，进行降序排列
rattings = rattings.sort_values('评分次数',ascending=False)
print(rattings)
print('-'*100)



# rattings.to_excel('../data/排序.xlsx')

# 采用布尔取值法，只取满足条件的数据
# 只取次数大于100的电影
rattings = rattings[rattings['评分次数']>100]
# rattings.to_excel('../data/排序_2.xlsx')
print(rattings)
print('-'*100)

#电影有9687部，用户有610人
#上面的表是根据 名称 进行分组，并分别计算出每一部电影的平均评分和评分次数，把只列出次数>100的数据
#评分次数较少的数据，我们认为有做弊的嫌疑


# 下面主要是为了求跟某部电影爱好，习好一致的数据，就是求相关性，1.0表示全相关，-1.0表示不相关
# 数据越接近于1.0，就表示相关度越高
# 就是看大家对某部电影的评分是否一致，表示相关性


# 创建透视图，以用户编号为索引，电影名称为列，内容为评分
# 列是特征
user_movie = df.pivot_table(index='用户编号',columns='名称',values='评分')
print(user_movie)

print('-'*100)
# 显示数量，平均值，标准差等信息
print(user_movie.describe())

print('-'*100)

# 取出勇敢者的游戏（1995）那一列，默认为series
FG = user_movie['阿甘正传（1994）']
# FG is  Series
print(type(FG))
print(FG)

print('-'*100)

print(pd.DataFrame(FG).head(n=5))

# # 利用前面讲到的corrwidh 函数计算 (阿甘正传)与其它电影的皮尔逊系数
# corr()是计算整张表的相关性
# corrwith(A)是计算整张表中其它物品和A物品之间的相关性
corr_FG = user_movie.corrwith(FG)
print('*'*100)
print(type(corr_FG))
corr_FG.name = '相关系数'
print(corr_FG)
print('-'*100)



similarity = pd.DataFrame(corr_FG,columns=['相关系数'])
# # 如果某部电影评分用户评价勇敢者的游戏用户一个交叉项也没有,则就无法计算协方差,形成空值
print(similarity)



print('-'*100)
# # 可以通过dropna删除控制   删除一些没有评分的数据
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



