
# 求两数之间的距离，即其差的绝对值
def dist(a, b):
    return abs(a-b)

# 数据属于哪一个集
def belong(v, set1, set2):
    r=2
    d1=dist(v,set1)
    d2=dist(v,set2)
    if d1<d2:
        r=1
    return r

# 求数据集的平均值
def avg(set):
    sum=0
    for i in range(len(set)):
        sum += set[i]

    return sum/len(set)

def mycalc(data, k1, k2):
    for i in range(100):
        print(f'迭代次数：{i+1}，K1 = {k1}, K2 = {k2}')

        set1=[]
        set2=[]
        for v in data:
            r=belong(v, k1, k2)
            if r==1:
                set1.append(v)
            else:
                set2.append(v)

        avg1=avg(set1)
        avg2=avg(set2)

        if ((dist(k1,avg1) < 0.00001) & (dist(k2,avg2) < 0.0001)):
            break

        k1=avg1
        k2=avg2

    pass


# 原始数据列表
data = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]

from sklearn.cluster import KMeans
import numpy as np


x = np.array(data)
print(x)


# 自己手工计算
print('自己手工计算：')
k1=16
k2=22
mycalc(data,k1,k2)


print('-'*100)
print('调用公式计算：')

# 调用K-means算法进行聚类处理
km = KMeans(n_clusters=2)

# 唯一一个在训练时不需要目标值的算法
# km.fit(l)
km.fit(x.reshape(-1,1))
#print(x.reshape(-1,1))


# k-means算法训练的过程就是找质心的过程
print(km.cluster_centers_)

