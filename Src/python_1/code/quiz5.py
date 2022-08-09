#关于类

#__new__ 申请内存空间
#__init__ 类对象进行初始化
#__del__ 析构对象
# 在Python中构造是用二个函数实现， __new__ + __init__


class MoneyCounter:

    def __new__(cls, *args, **kwargs):
        print("__new__")
        print(type(cls), cls)
        print(type(args), args)
        print(type(kwargs), kwargs)

        instance = super().__new__(cls)
        return instance


    def __init__(self, base=3000):
        self.base = base
        print("__init__")

    def __del__(self):
        print("__del__")

    def calc(self,a,b):
        return a+b+self.base


# 创建对象
c=MoneyCounter(4000)

print('-'*100)
print(c.calc(12, 34))
print('-'*100)

#销毁对象
del c



