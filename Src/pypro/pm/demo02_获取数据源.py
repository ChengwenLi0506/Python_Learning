import pandas as pd
from pandas import DataFrame
# numpy (数据 ndarray) pandas (index,columns), 加载数据,可视化
# pd.read_csv
# pd.read_excel
# pd.read_sql
# 变量:类型
df:DataFrame = pd.read_excel("../data/user.xls")
print(df.info())
print(df.head(n=3))

# 随机生成 940 [1,3] 随机数
import random
type_list = []
for i in range(940):
    # 数据追加到list中
    type_list.append(random.randint(1, 3))
print(len(type_list),type_list)
# 上面的功能可以通过列表解析式一步到位
type_list = [random.randint(1, 3) for i in range(940)]
print(len(type_list),type_list)
# 每一列就是Series
user_type = pd.Series(data=type_list)
# 新增加一列(类似dict语法)
df['user_type'] = user_type
print(df.head(n=3))
# dataframe重新保存 xls (第二次生成时user_2.xls文件要关闭)
df.to_excel(excel_writer="../data/user_2.xls",index=False)
