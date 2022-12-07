# java vs py 语法完全不同,但是编程思想完全一样
# 函数式编程 (函数) VS 面向对象编程  (属性、方法)

# s = 100000
# print(s,type(s))
# # s 里面存储 str类型的对象, 可以调用str类型定义的方法
# # 对象.方法  类.方法
# index = s.find(0)
# print(index)

# 面向对象本质就是对数据和数据的操作进行模块化(封装到类中)
# 创建一个类, 然后通过类构建对象
class Person():  # 官方定义类型默认都是小写 (str,list,dict,tuple,set..) 自定义类型采用驼峰命名法
    # 类: 只有 属性 + 方法
    # 双下划线开始和结束的方法称为魔法方法, 系统定义, 解决一些特殊功能
    __total = 2.0   # 变量和属性都要初始化, 静态属性和方法需要通过类调用

    @classmethod  # 类方法 --> 操作只能使静态属性
    def show_total(cls):
        return cls.__total

    # __init__用来进行对象的初始化
    def __init__(self,n1,a1):
        print('self:',self)
        # self == this 代表当前对象 (系统会自动赋值)
        self.name = n1   # 对象.属性 = 值
        # 如果双下划线开始则代表私有(类的外部不能访问),单下划线则受保护
        self.__age = a1

    @property  # @property 此装饰器可以让当前方法向属性一样使用 (只读)
    def age(self): # 方法
        return self.__age

    def show(self):
        print(f'name:{self.name},age:{self.age}')

p1 = Person("tom",25)   # ctrl + 单击  创建对象时默认会调用__init__方法
# print('name:',p1.name,'age:',p1.age)
p1.show()
print('p1:',p1)
print(Person.show_total())