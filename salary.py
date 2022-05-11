bs=int (input("enter your basic salary "))
if bs<10000:
    hra=(75/100)*bs
    ta=(70/100)*bs
    print ("salary is" ,bs+hra+ta)
elif bs>10000 and bs<20000:
    hra=(80/100)*bs
    ta=(80/100)*bs
    print ("salary is" ,bs+hra+ta)
elif bs>20000:
    hra=(90/100)*bs
    ta=(90/100)*bs
    print ("salary is" ,bs+hra+ta)
        
        
