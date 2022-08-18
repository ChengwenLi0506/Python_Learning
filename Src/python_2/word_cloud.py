# 加载txt文本
# import pandas as pd
# df = pd.read_csv("../data/text.txt")
# print(df)
with open("./text.txt",encoding="UTF-8") as f:
    contents = f.read()
print(contents)

# 1: 分词

#encoding=utf-8
import jieba
# for v in jieba.cut(contents):
#     print(v)
contents_cut = jieba.cut(contents)
contents_str = " ".join(contents_cut)
print(contents_str)
# 2: 统计
from sklearn.feature_extraction.text import CountVectorizer
vector = CountVectorizer()
# 可以对多篇文件进行统计
res = vector.fit_transform([contents_str])
print(vector.get_feature_names())
print(res.toarray())

from pyecharts import options as opts
from pyecharts.charts import WordCloud

words = [
    ("花鸟市场", 1446),
    ("汽车", 928),
    ("视频", 906),
    ("电视", 825),]

# 3: 可视化
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import WordCloud
num_array:np.ndarray = res.toarray()[0]
num_list = num_array.tolist()


words = [word for word in zip(vector.get_feature_names(), num_list)]
    #words.append(word)
print(words)
c = (
    WordCloud()
    .add(
        "",
        words,
        word_size_range=[20, 50],
        textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-自定义文字样式"),toolbox_opts=opts.ToolboxOpts(is_show=True))
    .render("./render.html")
)
