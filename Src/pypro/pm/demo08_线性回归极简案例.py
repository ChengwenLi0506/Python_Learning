# 传统数据分析 ---> 构建模型 (里面没有参数) --> 结果  ==> 数仓
# 人工智能 (模型有超参数,随着数据量,质量发生变化): 聚类,预测,分类
# 人工智能算法7个步骤:



# 4: 特征（列）: 统一量纲 (标准化，归一化), 主成分分析
# 5: 根据需求选择合适模型 (聚类,预测,分类)
# 6: 模型参数调优 (特征工程,模型参数)
# 7: 模型的保存与加载

import pandas as pd
# 1: 数据获取 (自有，爬虫，购买)
df = pd.read_csv("../data/house.csv")
print(df.info())
print(df.head(n=2))
# 2: 数据清洗 (numpy,pandas API 清洗数据)
X = df.drop(["price",'row_id'],axis=1)  # axis = 1 删除列
y = df['price']
print(X,y)
# 3: 把数据拆分训练集和测试 ==》 交叉验证
from sklearn.model_selection import train_test_split
# X_train,y_train 训练集特征值与目标值
# X_test,y_test 测试集特征值与目标值
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.25,random_state=1)
# 4: 特征（列）: 统一量纲 (标准化，归一化), 主成分分析
# 5: 根据需求选择合适模型 (聚类,预测,分类)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
# 对于线性回归模型,训练的权重与偏置
lr.fit(X_train,y_train)  # 训练模型,不同模型数学公式不同,因此训练的参数也不同
print(lr.coef_,lr.intercept_)
y_predict = lr.predict(X_test)
from sklearn.metrics import r2_score
# score: 0.9905150834257301
print('score:',r2_score(y_test,y_predict))