import numpy as np
import pandas as pd
# join merge连接操作
df1 = pd.DataFrame(data=np.array([['X', 1],
                                  ['Y', 2],
                                  ['Z', 3]]), columns=['key', 'v1'])
print(df1, type(df1))
# 采用字典方式创建DF,重要
# df2 = pd.DataFrame({'key': ['X', 'B', 'C'], 'v2': [4, 5, 6]})
df2 = pd.DataFrame({'key': ['X', 'B', 'C']})
df2['v2'] = [4, 5, 6]
print(df2, type(df2))
# 左右列符合条件的保留,不符合的过滤掉
print(pd.merge(df1, df2, on='key', how='inner'))
print(pd.merge(df1, df2, on='key', how='left'))
print(pd.merge(df1, df2, left_on='key', right_on='key', how='right'))
# 所有的key都保留,左右不匹配的设置为NAN
# print(pd.merge(df1, df2, left_on='key', right_on='key', how='outer'))
print('-'*40,'分组演示','-'*40)

import pandas as pd
df = pd.DataFrame(data=[['战狼2','丁一',6,8],
                       ['攀登者','王二',8,6],
                       ['攀登者','张三',10,8],
                       ['卧虎藏龙','李四',8,8],
                       ['卧虎藏龙','赵五',8,10]],columns=['电影名称','影评师','观前评分','观后评分'])
print(df)
# 每个组本质就是一张小表(tuple[0] 组名称, tuple[1] 当前组数据)
res = df.groupby("电影名称")
for v in res:
    print(v)
# 先分组,则聚合, groupby("key") 会自动转化为索引
ss = df.groupby("电影名称")['观前评分'].count()
print(ss.name,ss.index,ss.values)


print('-'*40,'透视图','-'*40)

import pandas as pd

df = pd.DataFrame(
  {
    "年份":[2019,2019,2019,2020,2020,2020],
    "平台":["京东","淘宝","拼多多","京东","淘宝","拼多多"],
    "销量":[100,200,300,400,500,600]
  }
)
print(df)
df = df.pivot_table(index='年份',columns='平台',values='销量')
print(df)


# similarity[similarity['评分次数'] > 20]
import numpy as np

t1 = np.arange(12).reshape(3,4)
print(t1[t1 > 6])