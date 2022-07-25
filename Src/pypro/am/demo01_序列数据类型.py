#  基本类型 (int str float bool)  序列类型: (list tuple dict set)  函数:(参数 重要)   类与对象(不重要)
#  numpy pandas 分析 matplotlib  pyecharts 可视化
#  sklearn 机器框架  tensorflow 深度框架   yolo 目标识别

# list: []  有序且支持重复
t = [1,2,3,4,1]
print(t,type(t))
t.append(100)
t.insert(0,-100)
print(t,type(t))
del t[0]
t[-1] = 10  # t[5]
print(t,type(t))

# tuple: () 只读list(有序且支持重复)
print('-'*100)
t = (1,2,3,4,1)
print(t,type(t))
# t[0] = 10 只读

# set: {} 没有下标(唯一)且不支持重复
s = {1,2,3,4,1}
print(s,type(s))
s.add(100)  # 没有append 因为无序
s.remove(2) # 无下标,则直接删除数据
print(s,type(s))

# dict : {}: 有无序下标 {key:value,key:value}

d = {'j':'java','p':'python'}  # dataframe里面格式就是dict
print(d,type(d))
print(d['j'])
d['o'] = 'oracle'
del d['j']
d['p'] = 'php'
print(d,type(d))




