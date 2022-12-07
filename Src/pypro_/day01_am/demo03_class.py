
class Person():  # 官方定义类型默认都是小写 (str,list,dict,tuple,set..) 自定义类型采用驼峰命名法

    # __init__用来进行对象的初始化
    def __init__(self,name,age):
        self.__name = name   # 对象.属性 = 值
        # 如果双下划线开始则代表私有(类的外部不能访问),单下划线则受保护
        self.__age = age

    def show(self):
        print(f'name:{self.__name},age:{self.__age}')

    # __ *() 代表是私有
    def __get_age(self):
        print('__get_age')
        return self.__age

    def __set_age(self,age):
        self.__age = age

    def __del_age(self):
        del self.__age

    # def __init__(self, fget=None, fset=None, fdel=None, doc=None):
    # 绑定了函数名,则后续可以反复调用
    age = property(fget=__get_age,fset = __set_age,fdel=__del_age)

p1 = Person("tom",25)
print(p1.age)
p1.age = 28
print(p1.age)
p1.show()
del p1.age
# p1.show()

