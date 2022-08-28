
import numpy as np
import pandas as pd

# # 消除警告信息
# import warnings
# warnings.filterwarnings(action="ignore")
#


# 1. 获取数据源：自有数据、购买数据例如万得、爬虫爬取数据
# 从文件中读取数据
df = pd.read_csv('../../data/house.csv')
print(df)
print('-'*100)

# 对于预测,分类需求需要区分X,y，即拆分自变量和因变量
y = df['price']

# axis : {0 or 'index', 1 or 'columns'}, default 0
X = df.drop('price',axis=1)

#和quiz8_1.py相比，只多出了这一句，去掉'row_id'的数据
X= X.drop('row_id', axis=1)

print(X)
print(y)
print('-'*100)

# 2. 清洗与预处理: (最耗时，空值、异常、抽样、相关性分析)
# 由于本数据已经预先处理过，不用再处理了，此步略

# 3. 拆分数据集：训练集 75% | 测试集 (未来) 25%
from sklearn.model_selection import train_test_split
# X_train,y_train: 训练集  特征值与目标值
# X_test,y_test:   测试集  特征值与目标值
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

print('训练集的数据：')
print(X_train)
print(y_train)
print('-'*100)

print('测试集的数据：')
print(X_test)
print(y_test)
print('-'*100)

# 4. 特征工程 (最重要)：标准化、归一化
# 由于本数据已经预先处理过，且比较简单，此步略

# 5. 训练模型：选择和训练模型 (聚类、回归、分类)
# 本例采用线性回归算法训练模块

from sklearn.linear_model import LinearRegression
lr = LinearRegression() # 创建 训练模型

print("开始训练模型 ... ...")
lr.fit(X_train,y_train) # 开始训练  训练的过程就是求权重和偏置的过程

# y = w1x1 + w2x2 + b
print(f'权重为: {lr.coef_}, 偏置为: {lr.intercept_}')
print('-'*100)


# 传入测试集数据，得到预测值
y_pred = lr.predict(X_test)

print("预测值：")
print(y_pred)
print("真实值：")
print(y_test.values)
print('-'*100)

# 下列对模型进行评估
# 预测值与真实值之差就是模型的误差
from sklearn.metrics import mean_squared_error   # mse
from sklearn.metrics import mean_absolute_error  # mae


print("MSE", mean_squared_error(y_test, y_pred))
print("MAE", mean_absolute_error(y_test, y_pred))
print("RMSE", np.sqrt(mean_squared_error(y_test, y_pred)))

print()
print("R2", lr.score(X_test, y_test))



# 6. 模型调优：超参数，特征工程
# 将在下面的代码中，对模型进行调优


# 7. 模型保存与加载：参数的保存、迁移学习
# 这只是一个一次性的实验例子，不用保存，此步略


