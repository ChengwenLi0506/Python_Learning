
#列表
v1=[1,2,3]
v2=['a','b','c']
print(type(v1), v1, v2)

#列表元素可以修改
v2[0]=100
print(type(v1), v1, v2)


#元组
v1=(1,2,3)
v2=('a','b','c')
print(type(v1), v1, v2)

#元组是只读的，不能修改
# v2[0]=100
# print(type(v1), v1, v2)


#集合
v1={1,2,3}
v2={'a','b','c'}
print(type(v1), v1, v2)

#集合元素不能重复，重复的元素被忽略
v1={1,2,3,2,1}
print(type(v1), v1, v2)

#字典
v1={'a':'attribute', 'b': 'business'}
v2={'a':['abc', 'attri', 'arise']}
print(type(v1), v1, v2)

#字典可以通过键来访问，不存在的键会自动添加，存在的键会自动修改
v1['b'] = '123'
v2['b'] = '123'
print(type(v1), v1, v2)

#字典中键只能有一个，但是值可以为多个，当值为多个时，采用列表形式展示
value = v2['a']
print(type(value), value)






