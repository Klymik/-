import math
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return x+math.sin(y/math.sqrt(10))

x0 = 0.6
h = 0.1
b=1.6
x=np.arange(x0,b+h,h)
n=len(x)-1
y=np.empty(n+1)
y[0]=0.8

for i in range(n):
    y[i+1]=y[i]+f(x[i],y[i])*h

print("x = ",np.round(x,1),"\ny = ",np.round(y,4))

plt.plot(x,y,'o',x,y,'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Ейлера')
plt.legend(['точки','x+sin(y/sqrt(10)'])
plt.show()