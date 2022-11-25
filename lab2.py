import numpy as np
import math
import matplotlib.pyplot as plt
def f(x):

    return 3*pow(x,4)-4*pow(x,3)-x*x-2*x-5

a = 1.
b = 2.
eps = 0.0001 #точність 

def dihotom(a, b, eps):

    while (abs(a-b) > eps):
        if f(a)*f((a+b)/2)<0:
            b = (a+b)/2
        else:
            a = (a+b)/2
    print('Корінь рівняння x = ', round((a+b)/2,5))

dihotom(a,b,eps)
x = np.arange(a, b, 0.0001)
plt.plot(x, f(x))
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Метод ділення навпіл')
plt.grid()
plt.show()