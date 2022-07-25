# 基本类型 （int str float bool)
# 序列 (list tuple dict set)
# 函数 参数 (参数 重要）
# 类型与对象

# numpy pandas  数据分析
# matplotlib  pyecharts 可视化
# sklearn 机器学习框架
# tensowflow 深度学习
# yolo 目标识别

# list: [] 有序且支持重复
t = [1,2,3,4,1]
print(t, type(t))
t.append(100)
t.insert(0, -100)
print(t, type(t))

del t[0]
print(t, type(t))
t[-1] = 10  #t[5]，最后一个
print(t, type(t))

# tuple: () 只读list (有序且支持重复）
print('-'*100)
t = (1,2,3,4,1)
print(t, type(t))
# t[0] = 10 error, 只读

#set: {} 没有下标（唯一）且不支持重复
s = {1,2,3,4,1,5}
print(s, type(s))
s.add(10)
print(s, type(s))
s.remove(2)
print(s, type(s))
#由于没有下标，所以只能对数据进行操作，不能操作位置


# dict: {} 有无序下标 {key:value, key:value}
print('-'*100)
d={'j':'jave','p':'python'}
print(d, type(d))

d = {'j':'java','p':'python'}  # dataframe里面格式就是dict
print(d,type(d))
print(d['j'])
d['o'] = 'oracle'
#del d['j']
d['p'] = 'php'
print(d,type(d))
# dict是以key为索引，相同的key只能存在一个值








