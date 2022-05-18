import numpy as np
out=([0,0],[0,0])
arr=np.array([2,3],[4,6])
for i in range (len(arr)):
    for j in range (len(arr)):
        out[i][j]=arr[j][i]+out[i][j]
print(out)        