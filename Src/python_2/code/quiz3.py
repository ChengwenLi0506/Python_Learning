

# 类的定义，三部分：class关键词， 类名（驼峰命名法），冒号：
class Counter:

    def __init__(self,name):
        print(name)
        self.name = name    # 成员变量，只要求用self. 开头就可以了

    def add(self,a,b):
        return a+b

#所有属于类的函数，必须缩进，这个是Python特有的极简语法




print('-'*30,'开始调用','-'*30)
c=Counter('1号')    # call __init__进行初始化
# c是一个类对象，所以对类的成员变量和方法的访问，就必须以类对象开头

print(type(c),c.name)
print(c.add(1,2))

print('-'*70)
c=Counter('2号')    # call __init__进行初始化
print(type(c),c.name)
print(c.add(100,2))


