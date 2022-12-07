
def gap(n):
    while n > 1:
        n = 1 if n <= 2 else 5 * n // 11
        yield(n)
# yield() 相当于把生砀元素放入一个元组中，调用一次，就放入一次


for step in gap(8):
    print(step)
# 3 1

for i in range(4,10):
    print(i)
# 4 5 6 7 8 9 10

for j in range(4, 4 - 1, -4):
    print(j)


a = [1,2,3,4,5,6,7,8]
pivot = (a[0] + a[len(a) // 2] + a[-1]) // 3

print(a[0], a[-1])

print(20*'-')
for n in range(8):
    print(n)
