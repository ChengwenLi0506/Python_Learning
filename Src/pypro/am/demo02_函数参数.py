# 函数: 参数非常重要:  必填, 缺省  不定长 (重要) 关键字 (重要)

def add(x,y):  # 必填,不灵活
    return x+y

print(add(4,5))
# 通过参数名赋值时,顺序不重要
print(add(y=5,x=2))

def add(x=10,y=20):  # 缺省,相对灵活
    return x+y

print(add(40,50))
print(add())
print(add(y = 20))  # 除了不定长,其它参数赋值可以通过名称赋值

print('-'*100)

# 函数定义时*代表不定长参数
def add(*num): # * 仅仅是修饰符, 变量名还是num
    print(type(num))
    sum = 0.0
    for v in num:  # 序列(存储多个数值)
        sum +=v
    return sum

# 传入多个值默认会通过tuple元组封装
print(add(1,2,3))

# 函数定义时**代表的是关键字参数 (会通过字典进行封装)
def add(name,age=23,**other):
    print(name,age,other,type(other))

add('A',address='上海',age_ = 34)