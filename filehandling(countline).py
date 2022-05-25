f=open("python.txt","r")
y=open("python.txt","r")
sum=0
a=f.read()
for i in a:
    sum=sum+1

wor=0
b=y.readlines()
for i in b:
    for j in i:
        if j==' 'or j=='\n':
            wor=wor+1


print(sum)
print(len(b))
print(wor)

f.close()
y.close() 

