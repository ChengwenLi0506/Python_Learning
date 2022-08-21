

# 词云图的几个关键步骤：
# 1, 分词       jieba  结巴分词模块
# 2，统计       分词后用空格隔开，然后利用另一个模块进行统计
# 3，可视化     统计出来的结果一定要跟可视化数据要求一样


# 加载txt文本
# 利用pandas读出来的是一个DataFrame，一行就是一个记录
# import pandas as pd
# df = pd.read_csv("../data/text.txt")
# print(type(df))
# print(df)

# 用文件打开的方式来读，读出来的数据是一个长字符串
with open("../data/text.txt",encoding="UTF-8") as f:
    contents = f.read()

print(type(contents))
print(contents)
print('-'*100)

# 1: 分词
# 接下来就是对长字符串进行分词，这里是利用一个工具库 jieba
# jieba 是可以对分词字典进行自定义的，作为演示，我们利用jieba内置的缺省字典 default dictionary

#encoding=utf-8
import jieba
# for v in jieba.cut(contents):
#     print(v)
contents_cut = jieba.cut(contents)
# contents_cut是一个类对象   <class 'generator'>
# print('-'*100)
# print(type(contents_cut),contents_cut)
# print('-'*100)

# 用空格将分词后的单词分隔开来，以方便显示和后续的处理
contents_str = " ".join(contents_cut)
print(contents_str)


# 2: 统计
# 从机器学习库sklearn 库中导入一个类CountVectorizer，可以对数据进行统计

from sklearn.feature_extraction.text import CountVectorizer
vector = CountVectorizer()

# 可以对多篇文件进行统计，参数是一个列表，可以输入多个字符串
res = vector.fit_transform([contents_str])
print(type(res))

# 会根据输入的参数，自动将空格隔开的每个单词作为feature，然后对feature出现的次数进行统计
# 统计的结果通过返回值传回

# 输出 每个单词
print(vector.get_feature_names())
# 输出 每个单词出现的次数
print(res.toarray())


print('-'*100)
print(len(vector.get_feature_names()))
print(len(res.toarray()[0]))
print('-'*100)



from pyecharts import options as opts
from pyecharts.charts import WordCloud

# 注意，词云图显示的数据格式是下在格式：
# 分为二层结构，最外层是list: [data1,data2,data3,]
#               里层是tuple: data1 = ('汽车’，322）
# words = [
#     ("花鸟市场", 1446),
#     ("汽车", 928),
#     ("视频", 906),
#     ("电视", 825),]

# 3: 可视化
import numpy as np

# feature name，也就是分词后的单词，已经是list
# 接下来，我们需要将res <class 'scipy.sparse.csr.csr_matrix'>也转成list
num_array:np.ndarray = res.toarray()[0] #得到第一篇文件的统计数据，是一个ndarry
num_list = num_array.tolist()           #将ndarry转成list

words = [word for word in zip(vector.get_feature_names(),num_list)]
print(words)

# 接下来调用pyecharts中的WordCloud组成词云图，将图保存在一个html文件中
c = (
    WordCloud()
    .add(
        "",
        words,
        shape = 'diamond',
        word_size_range=[10, 50],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="词云图 - 自定义文字样式"),
                     toolbox_opts=opts.ToolboxOpts(is_show=True))
    .render("../data/wordcloud_demo.html")
)





