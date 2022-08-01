#
# def swap(a, b):
#     return b, a
#
# a=3
# b=10
# print(a,b)
# a,b=swap(a,b)
# print(a,b)
#
#
# class Counter:
#     def __init__(self):
#         print("__init__")
#
#     def __del__(self):
#         print("__del__")
#
#     def add(self,a,b):
#         print('add')
#         return a+b
#
#
# x = Counter()
# x.add(4, 6)
# del x
#
#
import numpy as np
import pandas as pd
#
#
# print('-'*100)
# t1 = np.arange(16).reshape(4,4)  # ndarray 矩阵
# print(t1,type(t1),t1.shape)
#
# #t2 = pd.DataFrame(t1, index = ['a','b','c','d'], columns = ['M','N','O','P'])
# t2 = pd.DataFrame(t1, index = list('abcd'), columns = list('MNOP'))
# print(t2,type(t2))
#
#
# t3=t2['N']
# print(t3,type(t3))
#
# t4=t2.iloc[[1]
# #t4=t2.iloc[[1,2]]
# print(t4,type(t4))

# t1 = np.arange(16).reshape(4,4)  # ndarray 矩阵
# print(t1,type(t1),t1.shape)
#
# print('t1[1,3] = ', t1[1,3])
# print(type(t1[1,3]))
#
# t2=t1[1:3, 1:3]
# print(t2, type(t2))
#
# t3=t1[1:3, [1,3]]
# print(t3, type(t3))
#
# t4=t1[[1,3], 1:3]
# print(t4, type(t4))
#
# print('_'*100)
# d = {'M':[0,4,8,12],'N':[1,5,9,13],'O':[2,6,10,14],'P':[3,7,11,15]}
# print(d, type(d))
#
# #df = pd.DataFrame(data=d,index=['a','b','c','d'])
# df = pd.DataFrame(data=d,index=list('abcd'))
# print(df, type(df))

# data1={'name':['shan','shi','wu'],'age':[18,33,40]}
# data2={'name':['shan','shi', 'liu'],'height':[185,173,157]}
# a=pd.DataFrame(data=data1)
# b=pd.DataFrame(data=data2)
#
# print(a)
# print(b)
#
# print('-'*100)
# in_=pd.merge(a, b, on='name', how='inner')
# left_=pd.merge(a, b, on='name', how='left')
# right_=pd.merge(a, b, on='name', how='right')
# print(in_)
# print(left_)
# print(right_)


import math as mh

def ave(data):
    sum = 0
    for i in data:
        sum += i

    val = sum/len(data)
    return val

def squ(data):
    av = ave(data)
    sum = 0
    for i in data:
        sum += (i-av)*(i-av)

    val = sum / len(data)
    return val

def sta(data):
    tmp = squ(data);
    val = mh.sqrt(tmp)
    return val

def cov(d1, d2):
    a1 = ave(d1)
    a2 = ave(d2)
    sum = 0
    for i in range(len(d1)):
        sum += (d1[i]-a1)*(d2[i]-a2)

    val = sum / len(d1)
    return val

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

print(ave(d1))
print(ave(d2))

print('-'*100)
print(squ(d1))
print(squ(d2))

print('-'*100)
print(sta(d1))
print(sta(d2))


print('*'*100)

print(np.var(d1))
print(np.var(d2))

print('-'*100)
print(np.std(d1))
print(np.std(d2))

print('*'*100)
cov_= cov(d1,d2)
print("aaa:",cov_)
cov_2= cov2(d1,d2)
print("bbb:",cov_2)
# np.cov()


print('*'*100)
r = cov(d1,d2)/(sta(d1)*sta(d2))
print("ccc:",r)


from scipy.stats import pearsonr
# 采用官方皮尔逊公式
corr = pearsonr(d1,d2)
print("fff:", corr[0])


