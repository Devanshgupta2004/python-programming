n=int(input('enter number'))
a=0
b=1
for i in range(n):
    out=lambda a,b:a+b
    print(a)
    c=out(a,b)

    b=a
    a=c
