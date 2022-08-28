
import numpy as np
import pandas as pd

# 消除警告信息
import warnings
warnings.filterwarnings(action="ignore")


# 获取数据
df = pd.read_excel('../../data/mobile2.xls',index_col='基站编号')

# 对数据进行归一化
# from sklearn.preprocessing import MinMaxScaler
#
# # 此方式会吧dataFrame转化为ndarray类型
# mm = MinMaxScaler(feature_range=(0, 1))
# data = mm.fit_transform(df)

# 如果不想改变类型,这建议手动运算
data:pd.DataFrame = (df - df.min()) / (df.max() - df.min())

# 由于归一化，将商圈类别也改变了，需要恢复原来的商圈类别数据
data['商圈类别'] = df['商圈类别']

print(data)
print('-'*100)



# 准备对数据进行可视化
import matplotlib.pyplot as plt

#支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 配置每个张图的颜色值
style = ['ro-', 'go-', 'bo-']

# 配置后续用到的x轴的标签
xlabels = ['工作人均停留时间', '凌晨人均停留时间', '周末人均停留时间', '日均人流量']

# 生成图片输出路径，和名称
pic_output = "../../data/type_"

for i in range(3):
    tmp = data[data['商圈类别'] == i].iloc[:, :4] # 提取每一类别

    for j in range(len(tmp)):
        # 循环一次画一条线
        plt.plot(list('abcd'), tmp.iloc[j], style[i])
        plt.xticks(list('abcd'), xlabels,rotation=20)

    plt.savefig(f'{pic_output + str(i)}.png')
    plt.show()


