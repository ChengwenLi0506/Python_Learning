

#这个是常规的循环方法，用了三行语句来完成
numbers = []
for number in range(10):
    numbers.append(number)

print(numbers)

print('-'*100)



#这个是列表解析式，只用了一行语句来完成
numbers = [number for number in range(10)]

print(numbers)


