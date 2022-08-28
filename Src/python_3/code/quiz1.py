
# 我们先从最简单的机器学习入门

# 科学计算
import numpy as np

# 数据加载，处理，保存
import pandas as pd

# 可视化
import matplotlib.pyplot as plt

# 机器学习，主要是回归类和聚类K-means
from sklearn.linear_model import LinearRegression       # 线性回归
from sklearn.preprocessing import PolynomialFeatures    # 多项式回归
from sklearn.cluster import kmeans_plusplus             # 聚类K-means
# 评价指标
from sklearn.metrics import mean_squared_error          # mse
from sklearn.metrics import mean_absolute_error         # mae
# 测试数据集
from sklearn.datasets import load_boston                # boston


