

#普通函数
# 函数的定义包括四部分：def关键词，函数名（一般用小写），参数（放到一组括号内），以及结尾的冒号：
def add(a, b):
    print("it is a function")
    print(a, b)
    return a+b


#类方法
class Counter:

    def __init__(self, base=100):
        print("initialize a class object")
        self.base = base

    # 类方法
    def add(self, a, b):
        print("it is a class method")
        print(a, b)
        return a+b+self.base



#调用
print(add(1,2))

print('-'*100)
c=Counter()
print(c.add(1,2))




