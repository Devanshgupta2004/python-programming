l = [('ram', 45), ('shyam', 68), ('madhav', 97), ('ajay', 4)]


for i in range (len(l)):
    for j in range (i+1,len(l)+1):

        if l[i][i] > l[j][j]:
            temp = l[i][i]
            l[i][i] = l[j][j]
            l[j][j] = temp



print(l)
            


