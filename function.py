# def febo(x):
#     f=0
#     s=1
#     print(f, s,'',end='')
#     for i in range(x-2):
#         sum=f+s
#         print( sum,end=' ')
#         f=s
#         s=sum

# num=int(input("Enter a no.(>3)"))
# febo(num)

# def rev(x):
#     temp=x
#     count=0
#     st=" "
#     while temp!=0:
#         z=temp%1
#         st=st+str(z)
#         temp=temp//10
#     print("Reverse:",st)


# num=int(input("Enter a no."))
# rev(num)

def pali(k):
    re=k[::-1] 
    return re

st=input("enter a string")
m=pali(st)
if m==st:
    print("Palindrome")
else:
    print("Not palindrome")
