f=open("seven.txt","w")
y=open("python.txt","r")
a=y.readlines()
for i in range(len(a)):
    if i%2!=0:
        f.write(a[i])
f.close()
y.close()        