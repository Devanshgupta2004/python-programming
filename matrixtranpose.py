import numpy as np
m=[2,3,4],[4,5,6],[7,8,9]

arr=np.array(m)
out=[[0]*(len(arr))for i in range (len(arr))]
for i in range (len(arr)):
    for j in range (len(arr)):
        out[j][i]=arr[i][j]
print(arr) 
print(out)  
     
