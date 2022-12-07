# 函数式编程  VS 面向对象编程


# 对象.方法
# 类.方法

class Person():
    __total = 2.0

    @classmethod
    def show_total(cls):
        return cls.__total

    def __init__(self, n1, a1):
        self.__name = n1
        self.__age = a1

    def __get_age(self):
        return self.__age;

    def __set_age(self, age):
        self.__age = age;

    def __del_age(self):
        del self.__age

    age = property(fget=__get_age, fset=__set_age, fdel=__del_age)





p1 = Person("tom", 25)
print(p1.age)
p1.age = 30
print(p1.age)

