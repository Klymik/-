import math
import numpy as np
x = [2.4,2.6,2.8,3.0,3.2,3.4]
y = [3.526,3.782,3.945,4.043,4.104,4.155]
h = x[1] - x[0]
print ("h = ",h)
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
y1 = 1/ h * (n(y,1)[1] - (n(y,2)[1]/2) + (n(y,3)[1]/3) - (n(y,4)[1]/4))
y2 = 1/ (h**2) * (n(y,2)[1] - n(y,3)[1] + 11/12*n(y,4)[1]) 

print ('First derivative =', y1)
print ('Second derivative =', y2)    
