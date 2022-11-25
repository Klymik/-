import numpy as np
from math import factorial

x=[0, 0.15, 0.20, 0.25, 0.30, 0.35]
y=[0.8607 ,0.8187, 0.7788, 0.7408, 0.7046, 0.6703]
h = x[1] - x[0]
x1=0.457
x2=0.151
q=(x1 - x[0])/h
q1 = (x2-x[-1])/h
def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)  
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)
s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4
print ('The value of a function at a point x1=', x1, 'using Newton*s First Interpolation Formula', round(n_1,5))
m_1 = y[5]+q1*n(y,1)[4]
m_2 = ((q1*(q1+1))/factorial(2))*n(y,2)[3]
m_3 = ((q1*(q1+1)*(q1+2))/factorial(3))*n(y,3)[2]
m_4 = ((q1*(q1+1)*(q1+2)*(q1+3))/factorial(4))*n(y,4)[1]
n_2 = m_1 + m_2 + m_3 + m_4
print ('The value of a function at a point x1=', x1, 'using Newton*s Second Interpolation Formula', round(n_2,5))
