import matplotlib.pyplot as plt
import pandas as pd

df:pd.DataFrame = pd.read_excel("mobile2.xls", index_col="基站编号")
plt.rcParams['font.sans-serif'] = ['SimHei']
# 配置每个张图的颜色值
style = ['ro-', 'go-', 'bo-']
# 配置后续用到的x轴的标签
xlabels = ['工作人均停留时间', '凌晨人均停留时间', '周末人均停留时间', '日均人流量']
pic_output = "type_"
print('-' * 100)
for i in range(3):
    tmp = df[df['基站类别'] == i].iloc[:, :4] # 提取每一类别
    for j in range(len(tmp)):
        # 循环一次画一条线
        plt.plot(xlabels, tmp.iloc[j], style[i])
    plt.savefig(f'{pic_output + str(i)}.png')
    plt.show()