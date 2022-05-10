import math
def fact_sum(*n):
    
    def fact():
        sum1=0
        for i in n:
            sum1=sum1+math.factorial(i)
        return sum1
    sume=fact()        
    return sume    

a=fact_sum(0,1,2,3,4)
print(a)


    