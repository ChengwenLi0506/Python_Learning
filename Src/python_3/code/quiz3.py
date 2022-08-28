
# 本代码演示print的几种输出格式

# 1，print()常用方法
# print()函数是一个标准格式化输出函数
# print(*object(s), sep=’’,end=’\n’, file = sys.stdout, flush =
print('-'*100)

print("Hello World")

# 如果是字符型，可以用+进行拼接
name = "李白"
age = '2000'
print("他的名字叫"+name+",今年"+age+"岁")

# 如果不是字符，则需要用str函数进行转换
name = "李白"
age = 2000
print("他的名字叫"+name+",今年"+str(age)+"岁")

# 用格式化控制显示
pi = 3.1415926
print('圆周率为：%f' % pi) #默认输出小数点后面6位
print('圆周率为：%.0f' % pi)
print('圆周率为：%.2f' % pi)
print('圆周率为：%.3f' % pi)
print('圆周率为：%.8f' % pi) #不足位用0补足


# 2， format()函数，根据顺序填入{}内

print('-'*100)

print('{} {}'.format('hello','python'))
print('{0} {1}'.format('hello','world'))
print('{1} {0} {1}'.format('hello','world'))

print('ID:{id},Name:{name}'.format(id='001',name='hello'))


# 3，f-string，亦称为格式化字符串常量（formatted string literals），
# 是Python3.6新引入的一种字符串格式化方法

print('-'*100)

name = '李白'
print(f'Hello, my name is {name}')

price = 19.99
print(f'The price of this book is {price}')

print(f'A total number of {24 * 8 + 4}')

name = 'ERIC'
print(f'My name is {name.lower()}')





