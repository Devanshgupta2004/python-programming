m=list(map(int,input("enter list").split()))
min=m[0]
for i in m:
    if i<min:
        min=i
print ("smallest number is",min)        
