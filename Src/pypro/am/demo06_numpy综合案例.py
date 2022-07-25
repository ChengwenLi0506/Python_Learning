# 通过Numpy运算,完成图像的处理
import numpy as np
# from numpy import array,arange
from PIL.Image import open,fromarray
# 1: 图像加载的内存
img = open("../data/pic.jpeg")
print(img,type(img))
# 2: image转化ndarray
img = np.array(img)
print(img,type(img),img.shape)
# 3: 运算获取互补色  # [0~255]
img = 255 - img
# 3: 通过切片获取指定的数据
img = img[:,1080//2:]
# 4: ndarray转化为内存的图片
img = fromarray(img)
print(img,type(img))
# 5: 把img保存到硬盘
img.save("../data/pic2.jpeg")
