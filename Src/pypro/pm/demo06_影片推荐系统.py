import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# movies = pd.read_excel("../data/电影.xlsx")
# score = pd.read_excel("../data/评分.xlsx")
# print(movies.info())
# print(movies.head(n=5))
# print(score.info())
# print(score.head(n=5))
# # 默认内连接: how='inner', on=None
# df = pd.merge(movies,score,on='电影编号',how="inner")
# df.to_excel('../data/电影推荐系统.xlsx',index=False)

df = pd.read_excel('../data/电影推荐系统.xlsx')

# df已经合并的数据
# 按照名称归类,采用mean聚合函数计算每部电影的评分均值。
rattings = pd.DataFrame(df.groupby('名称')['评分'].mean())
rattings = rattings.sort_values('评分',ascending=True) # 升序排列
# "名称"(电影名称) 就是 index 索引
print(rattings)  # asc 升序  desc 降序
# df['列名'] = value 新增一列
rattings['评分次数'] = df.groupby('名称')['评分'].count()
rattings = rattings.sort_values('评分次数',ascending=False)
print(rattings)
print('-'*100)

#                             评分  评分次数
# 名称  (电影名称)
# 阿甘正传（1994）              4.164134   329
# 肖申克的救赎（1994）            4.429022   317
# 低俗小说（1994）              4.197068   307
# 沉默的羔羊（1991）             4.161290   279
# 黑客帝国（1999）              4.192446   278

# # 用户编号作为数据透视图索引,设置columns参数为'名称', 设置评分作为作为透视图显示的数据
user_movie = df.pivot_table(index='用户编号',columns='名称',values='评分')
# # i行j列单元格中的值代表第i个用户对第j部电影的评分,可以看到绝大部分评分是NAN
# # 是一个稀疏矩阵 (电影过于庞大,而每个用户打分的电影数量却很有限)
print(user_movie)

# 名称    007之黄金眼（1995）  100个女孩（2000）  ...  龙：李小龙的故事（1993）  龟日记（1985）
# 用户编号                               ...
# 1               NaN           NaN  ...             NaN        NaN
# 2               NaN           NaN  ...             NaN        NaN
# 3               NaN           NaN  ...             NaN        NaN

print('-'*100)
# # count: 改电影评分次数, mean 平均值  std 标准差
FG = user_movie['阿甘正传（1994）']
# print(pd.Series(FG))
# # 此处返回的是一个Series序列,电影名称为index,皮尔逊系数为value值
corr_FG = user_movie.corrwith(FG)
# # 利用前面讲到的corrwidh 函数计算 (阿甘正传)与其它电影的皮尔逊系数
corr_FG.name = '相关系数'
# similarity = pd.DataFrame(corr_FG,columns=['相关系数'])
# # 如果某部电影评分用户评价阿甘正传用户一个交叉项也没有,则就无法计算协方差,形成空值
# # 可以通过dropna删除空值
corr_FG = corr_FG.dropna()
print(corr_FG)

# 名称
# 007之黄金眼（1995）         0.217441
# 101忠狗（1961）           0.141023
# 102只斑点狗（2000）        -0.857589
# 10件或更少（2006）         -1.000000
# 11:14（2003）           0.500000

similarity = pd.merge(corr_FG,rattings['评分次数'],left_index=True,right_index=True)
# # 功能同上,默认按索引进行合并
# # similarity_new = similarity.join(rattings['评分次数'])
similarity_new = similarity[similarity['评分次数'] > 20].sort_values(by='相关系数',ascending=False)
print(similarity_new.head(n=10))