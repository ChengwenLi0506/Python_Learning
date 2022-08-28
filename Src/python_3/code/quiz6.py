
# 机器学习，主要是回归类和聚类K-means
from sklearn.linear_model import LinearRegression       # 线性回归
from sklearn.preprocessing import PolynomialFeatures    # 多项式回归
from sklearn.cluster import kmeans_plusplus             # 聚类K-means



# 回归类算法对数据的处理
# 1. 对现有数据进行拆分，按比例分成二块：训练集和测试集
# 2. 对训练集的数据进行回归和迭代，以找到自变量组（一般是多维数据）和因变量（一般是一维数据）之间的关系
# 3. 这个关系就是模型，就是权重W和截距b
# 4. 然后再将测试集的自变量组代入模型 （注意，只能找入自变量，因为是预测）
# 5. 得出的结果叫预测值
# 6. 然后比较预测值 和 测试集中的真实值，得到评估结果
# 7. 根据评估结果，返回去整理数据，重建模型，这就是模型的调优
# 8. 当模型满意后，则保存模型
# 9. 然后对未来数据  （此时只有自变量，没有因变量）进行预测
#
#


