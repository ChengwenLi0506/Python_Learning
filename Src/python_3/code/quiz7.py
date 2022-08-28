
import math


# MSE   真实结果和预测结果误差的平方的均值, 也叫做均方误差, 这种方式会将误差扩大一倍
def mse(y_true, y_pred):
    sum = 0.0
    for i in range(len(y_true)):
        sum += (y_true[i]-y_pred[i])**2

    return sum/len(y_true)

# RMSE   是在MSE的结果上开平方，也叫均方根误差
def rmse(y_true, y_pred):
    result = mse(y_true, y_pred)

    return math.sqrt(result)

# MAE   平均绝对误差，解决了MSE误差扩大的问题
def mae(y_true, y_pred):
    sum = 0.0
    for i in range(len(y_true)):
        sum += abs((y_true[i]-y_pred[i]))

    return sum/len(y_true)

# 求一组数据的平均值，为辅助函数
def avg(value):
    sum = 0.0
    for i in range(len(value)):
        sum += value[i]

    return sum/len(value)

# R2 决定系数，描述了准确率，越接近1，表示越准确
def rtwo(y_true, y_pred):
    tmp = avg(y_true)
    u = 0.0
    v = 0.0
    for i in range(len(y_true)):
        u += (y_true[i]-y_pred[i])**2
        v += (y_true[i]-tmp)**2

    return 1-u/v




# 构造数据
# 假设y_true是真实结果数据, y_pred是预测结果数据
y_true = [174.3, 194.2]  # 准确值
y_pred = [171.1, 185.3]  # 预测值

print('自己计算的结果')
print("MAE: ", mae(y_true, y_pred))
print("MSE: ",  mse(y_true, y_pred))
print("RMSE: ", rmse(y_true, y_pred))
print("R2: ", rtwo(y_true, y_pred))

print('-'*100)

from sklearn.metrics import mean_squared_error  # mse
from sklearn.metrics import mean_absolute_error  # mae

print('调用工具库计算的结果')
print("MAE: ", mean_absolute_error(y_true, y_pred))
print("MSE: ", mean_squared_error(y_true, y_pred))
print("RMSE: ", math.sqrt(mean_squared_error(y_true, y_pred)))


# 机器学习库中并没有提供直观的R2
# 而是集成在预测过程中，所以我们要模拟线性回归的过程进行预测

import numpy as np
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

y_test = np.array(y_true).reshape(-1,1)
lr.fit(y_test, y_test)


# print("回归系数：", lr.coef_)
# print("回归截距：", lr.intercept_)

x_test = np.array(y_pred).reshape(-1,1)
print("R2: ", lr.score(x_test, y_test))

