from random import random
 
def srarifm(a):
    return sum(a) / len(a)
 
n = int(input("N: "))
m = int(input("M: "))
A = []
 
for i in range(n):
    arr = []
    for j in range(m):
        arr.append(int(random() * 10))
    A.append(arr)
B = []
for arr in A:
    print(arr,"Середнє: ", srarifm(arr))
    B.append(srarifm(arr))
print("Мінімальне середнє: ", min(B))