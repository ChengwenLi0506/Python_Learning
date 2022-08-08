
#必填
def show(name, age):
    print(name, age)

show('zhangshan', 30)
#show('zhangshan')

print('-'*100)

#缺省
def show(name='people', age=18):
    print(name, age)

show('zhangshan', 30)
show('zhangshan')
show(20)
show(age=20)
show()

print('-'*100)


#不定长，用一个星表示
def show(*data):
    print(type(data), data)

show(1,2,3,4)
show('A','B','C',1,2,3,4)

print('-'*100)

#关键字，用二个星表示
def show(**age):
    print(type(age), age)


show(age=30)
show(age=30, people='123')

print('-'*100)

#函数返回值
def switch(a, b):
    return b, a

ret = switch(1,4)
print(type(ret), ret)

a,b = switch(1,4)
print(type(a), a, type(b), )


