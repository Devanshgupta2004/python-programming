
lst1=list(map(int,input("enter list").split()))
lst2=list(map(int,input("enter list").split()))
lst3=[0 for i in range(len(lst1))]
if len(lst1)==len(lst2):
    for i in range(len(lst1)):
        lst3[i]=(lst1[i],lst2[i])
    print(lst3)    
else:
    print("ivalid lenght lenght should be equal")        
   
