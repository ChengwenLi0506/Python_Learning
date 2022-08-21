

class Counter:

    # public 方法
    def add(self, a, b):
        return a+b

    # protected 方法
    def _addself(self, a):
        a=self.__add100(a)
        return a+1

    # private 方法，只能被类中方法调用，外部不可以调用
    def __add100(self, a):
        return a+100

    # system 方法，可以重载，如果想调用基类的，则用super()
    def __init__(self, base=100):
        print("it is same as the constructor in C++")
        self.base = base



c = Counter()
print(c.add(1, 2))

print(c._addself(123))

# c.__add100(1)


