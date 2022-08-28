
# 科学计算
import numpy as np

a1 = np.arange(16).reshape(4,4)
print('初始矩阵：')
print(a1)

# 矩阵乘法运算
print('-'*100)
print('矩阵乘法')

a2=a1
print(a2)
a3=a1*a2
print(a3)

print('-'*50)

a2=a1[0,]
print(a2)
a3=a1*a2
print(a3)


print('-'*50)

a2=a1[:,0].reshape(4,1)
print(a2)
a3=a1*a2
print(a3)

print('-'*50)
a2=10
print(a2)
a3=a1*a2
print(a3)







