from re import X
import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
b=np.array(a)
for i in range( len(b)):
    for j in range(len(a)):
        g=i+j
        if g%2==0:
            a[i][j]="devansh"
print(a)            

