import math
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x+math.cos(y/2.25)

x0 = 1.4
h = 0.1
b=2.4
x=np.arange(x0,b+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=2.2

for i in range(n):
    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],y[i]+h*f(x[i],y[i])))*h/2

print("x = ",np.round(x,1),"\ny = ",np.round(y,4))

plt.plot(x,y,'o',x,y,'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Ейлера-Коші')
plt.legend(['точки','x+cos(y/2.25)'])
plt.show()