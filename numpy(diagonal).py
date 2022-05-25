import numpy as np
m=[1,2,3],[3,4,5],[4,5,6]
arr=np.array(m)
sum=0
for i in range (len(arr)):
    for j in  range(len(arr[1])):
        if i==j:
            sum=sum+arr[i][j]
print(sum)            
