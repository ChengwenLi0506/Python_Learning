import matplotlib.pyplot as plt
import numpy as np



# make data
X, Y = np.meshgrid(np.linspace(-3, 3, 16), np.linspace(-3, 3, 16))
Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2)

# plot
fig, ax = plt.subplots()

ax.imshow(Z)

plt.show()

#这里只是演示了最后的显示是调用imshow，完整的词云图会在quiz12中进行演示



