import matplotlib.pyplot as plt
from math import sin, radians
x = []
y = []
for n in range(0, 361):
    x.append(n)
    y.append(sin(radians(n)))

plt.plot(x,y)
plt.show