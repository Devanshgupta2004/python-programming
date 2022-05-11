# def iseven(n):
#     if(n%2==0):
#         return True
#     else: 
#         return False   
# n=int(input())
# print(iseven(n))
########################################Upper case
# def toupper(s):
#         for i in s:
#             print(chr(ord(i)-32),end="")
# s=input()
# toupper(s)      
# #######################################lower case
# def tolower(s):
#         for i in s:
#             if(i>='A'and i<='Z'):
#                  print(chr(ord(i)+32),end="")
#             else:
#                 print(" ",end="")    
# s=input()
# tolower(s)
##########################################
# def isprime(n):
#         flag=0
#         for i in range(2,n//2):
#             if(n%i==0):
#                 flag=1
        
#         if(flag==1):
#             return False
#         else:
#             return True      

# n=int(input())   

# if(isprime(n)):
#     print("prime")
# else:
#     print("not prime")    
##############################################
from itertools import count


def armstrong(lb,ub):
    for i in range(lb,ub):
          dg=0
          dg=len(str(i))
          sum=0
         
          num=i
          while(i>0):
              r=i%10
              sum=sum+pow(r,dg)
              i=i//10
          if(sum==num):
              print(num,end=" ")   

lb=int(input("enter lower value="))
ub=int(input("enter uper value="))
armstrong(lb,ub)