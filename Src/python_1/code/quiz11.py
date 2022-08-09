
import numpy as np
import pandas as pd
import math as mh

# 自己计算平均值
def ave(data):
    sum = 0
    for i in data:
        sum += i

    val = sum/len(data)
    return val


# 自己计算方差
def squ(data):
    av = ave(data)
    sum = 0
    for i in data:
        sum += (i-av)*(i-av)

    val = sum / len(data)
    return val


# 自己计算标准差
def sta(data):
    tmp = squ(data);
    val = mh.sqrt(tmp)
    return val


# 自己计算协方法，使用定义式
def cov(d1, d2):
    a1 = ave(d1)
    a2 = ave(d2)
    sum = 0
    for i in range(len(d1)):
        sum += (d1[i]-a1)*(d2[i]-a2)

    val = sum / len(d1)
    return val


# 自己计算协方差，使用推理式
def cov2(x, y):
    ex = ave(x)
    ey = ave(y)

    xy=[]
    for i in range(len(x)):
        tmp = x[i]*y[i]
        xy.append(tmp)

    exy = ave(xy)
    val = exy-ex*ey
    return val






d1=[50,100,100,60,50]
#d2=[50,100,100,60,50]
d2=[73,70,75,72,70]

print('calc 平均值 by myself')
print(ave(d1))
print(ave(d2))

print('calc 平均值 by mean api')
print(np.mean(d1))
print(np.mean(d2))

print('calc 平均值 by average api')
print(np.average(d1))
print(np.average(d2))

# mean() 和 average的区别，在于mean可以做加权平均

print('-'*100)

print('calc 方差 by meself')
print(squ(d1))
print(squ(d2))

print('calc 方差 by var api')
print(np.var(d1))
print(np.var(d2))



print('-'*100)

print('calc 标准差 by meself')
print(sta(d1))
print(sta(d2))

print('calc 标准差 by std api')
print(np.std(d1))
print(np.std(d2))


print()
print('*'*100)

cov_= cov(d1,d2)
print("方法一的协方差:  ",cov_)
cov_2= cov2(d1,d2)
print("方法二的协方差:  :",cov_2)


print('-'*100)
r = cov(d1,d2)/(sta(d1)*sta(d2))
print("自己计算皮尔逊系数:  ",r)


from scipy.stats import pearsonr
# 采用官方皮尔逊公式
corr = pearsonr(d1,d2)
print("采用官方公式计算皮尔逊系数:  :", corr[0])



