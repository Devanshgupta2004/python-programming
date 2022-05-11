from re import A


m=list(map(int,input("enter list").split()))
a=m[0]
b=m[-1]
m[-1]=a

m[0]=b
print ("list after swappinr ",m)