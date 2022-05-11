a=int(input("enter your reading"))
x= 50*0.2
y=100*0.5
z=100*1.20
k=(a-250)*1.75
if a<50:
    print (x)
elif a<=150:
    print(x+(a-50)*0.5)
elif a<=250:
    print(x+y+(a-150)*1.20)
elif a>250:
    print(x+y+z+(a-250)*1.75)    
    
