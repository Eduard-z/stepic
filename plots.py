from pylab import *
from numpy import *

a = array([(2, 3, 4), (3, 4, 5)])
print(a)
print(a.ndim)
print(a.shape)
z = zeros((3, 2))
print(z)
b = arange(10, 30, 5)
print(b)
c = linspace(0, 2, 8)
print(c)
print(b < 20)


x = linspace(0, 5, 10)
y = x ** 2
print(x)
print(y)

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()

fig, ax = plt.subplots()
ax.plot(x, x ** 2, label="y = x**2")
ax.plot(x, x ** 3, label="y = x**3")
ax.legend(loc=2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
show()

n = random.randn(100000)
fig, axes = subplots(1,2,figsize=(12,4))
axes[0].hist(n)
axes[0].set_title('Default histogram')
axes[0].set_xlim((min(n),max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title('Cumulative detailed histogram')
axes[1].set_xlim((min(n),max(n)))
show()
