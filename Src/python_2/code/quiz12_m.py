

# wordcloud 是另一个处理词云图的库，我们加载它，利用它来生成词云图
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

import os
import jieba
import random
import numpy as np

from os import path
from PIL import Image
from matplotlib import pyplot as plt



f = open("../data/text.txt",encoding="UTF-8")
f1 = f.read()
f.close()


print(f1)

#将句子分为字符串
f2 = jieba.cut(f1)
print(f2)
f3 = ' '.join(f2)
print(f3)

# 以上步骤跟前面利用pyecharts绘制词云的过程完全一样
# 是准备数据的阶段，跟具体的绘制没有关系


stopwords = set(STOPWORDS)
stopwords.add('的')
stopwords.add('是')
stopwords.add('这')
stopwords.add('都')

#创建词云图对象
f4 = WordCloud(font_path='C:/Windows/Fonts/msyhl.ttc',
               width=400,height=300,
               margin=0,
               stopwords=stopwords,
               background_color='red').generate(f3)
plt.imshow(f4)


#控制坐标轴是否显示
plt.axis('off')
plt.show()




# 读取背景图片
background_Image = np.array(Image.open("../data/mask1900.jpg"))
# 提取背景图片颜色
img_colors = ImageColorGenerator(background_Image)

#创建词云图对象
f4 = WordCloud(font_path='C:/Windows/Fonts/msyhl.ttc',
               width=400,height=400,
               margin=0,scale=1,
               stopwords=stopwords,
               mask=background_Image,
               background_color='white').generate(f3)
plt.imshow(f4)


#控制坐标轴是否显示
plt.axis('off')
plt.show()




# 1 wordcloud.WordCloud(
# 2 font_path=None, # 字体路径，英文不用设置路径，中文需要，否则无法正确显示图形
# 3 width=400, # 默认宽度
# 4 height=200, # 默认高度
# 5 margin=2, # 边缘
# 6 ranks_only=None,
# 7 prefer_horizontal=0.9,
# 8 mask=None, # 背景图形，如果想根据图片绘制，则需要设置
# 9 scale=1,
# 10 color_func=None,
# 11 max_words=200, # 最多显示的词汇量
# 12 min_font_size=4, # 最小字号
# 13 stopwords=None, # 停止词设置，修正词云图时需要设置
# 14 random_state=None,
# 15 background_color='black', # 背景颜色设置，可以为具体颜色,比如white或者16进制数值
# 16 max_font_size=None, # 最大字号
# 17 font_step=1,
# 18 mode='RGB',
# 19 relative_scaling='auto',
# 20 regexp=None,
# 21 collocations=True,
# 22 colormap='viridis', # matplotlib 色图，可更改名称进而更改整体风格
# 23 normalize_plurals=True,
# 24 contour_width=0,
# 25 contour_color='black',
# 26 repeat=False)








