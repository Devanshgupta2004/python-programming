m=list(map(int,input("enter space sperated value").split()))
odd=0
even=0
for i in m:
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print ("sum of even digit are ",even)
print ("sum of odd digit are ",odd)  
