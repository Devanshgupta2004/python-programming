n= int( input(" entre row"))
for i in range (1,n+1):
    if i==1 or i==n:
        for i in range(1,n+1):
            print('*',end='')
    else:
         for i in range(1,n+1):
             if i==1 or i==n:
                 
                 print('*',end='')
             else:    
                 print(' ',end='')
                 
          
    print()
         
            
