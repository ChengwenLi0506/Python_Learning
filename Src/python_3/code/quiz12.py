
# 机器学习的7大步骤

import numpy as np
from sklearn.datasets import load_boston
from sklearn.preprocessing import PolynomialFeatures

# 1. 获取数据源：自有数据、购买数据例如万得、爬虫爬取数据
# 在sklearn.datasets数据集中获取boston房屋价格数据
lb = load_boston(return_X_y=False)
# print(lb,type(lb))

# 获取特征值(自变量）和目标值(因变量)
X = lb['data']
y = lb['target']
print(X.shape,y.shape)

# 多项式升级（二次多项式）
pf = PolynomialFeatures(degree=2,include_bias=False)
print('整合前的特征维度：', X.shape)
X = pf.fit_transform(X)
print('整合后的特征维度：', X.shape)


# 2. 清洗与预处理: (最耗时，空值、异常、抽样、相关性分析)
# sk-learn为了模型的学习，官方提供了很多训练数据，不用另外的清洗

# 3. 拆分数据集：训练集 75% | 测试集 (未来) 25%
from sklearn.model_selection import train_test_split
# X_train,y_train: 训练集  特征值与目标值
# X_test,y_test:   测试集  特征值与目标值
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# 4. 特征工程 (最重要)：标准化、归一化
# 由于数据进行了多项式处理，有的是一次项，有的是多次项，量纲不同了，所以要进行标准化处理
from sklearn.preprocessing import StandardScaler
std_x = StandardScaler()
X_train = std_x.fit_transform(X_train)
X_test = std_x.transform(X_test)

# 5. 训练模型：选择和训练模型 (聚类、回归、分类)
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
print(y_test)
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

# 7. 模型保存与加载：参数的保存、迁移学习





