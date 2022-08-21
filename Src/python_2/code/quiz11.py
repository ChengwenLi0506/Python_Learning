
# 机器学习库 sklearn

# from 包.包.模块 import 函数
from sklearn.datasets import load_iris

# from 包.包.模块 import 类
# 只有类的命名,采用驼峰命名法
from sklearn.utils import Bunch

df = load_iris()
print(type(df),'\n',df.keys())


T = df['data']  # 特征
y = df['target'] # 分类


# 150样本4个特征，前二个是萼片的长和宽，后二个是花瓣的长和宽
print(T,'\n',T.shape)
# 150样本类别值
print(y,'\n',y.shape)



import matplotlib.pyplot as plt


# 采用散点图完成可视化
X = T[:,:2] #  获取萼片的特征

plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])
plt.scatter(X[y==2,0],X[y==2,1])
plt.show()



X = T[:,2:] #  获取花瓣的特征

plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])
plt.scatter(X[y==2,0],X[y==2,1])
plt.show()


# 这个就是典型的数据分析，排除不相关的特征项
# 四组数据
#   分成二组，分别表示 萼片和花瓣
#       每一组再分为长度和宽度

# [萼片的长度，萼片的宽度，花瓣的长度，花瓣的宽度]






