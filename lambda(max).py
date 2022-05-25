a =  int(input("enter the value of a \n"))
b = int(input("enter the value of b \n"))


z = lambda a,b : a if a>b else b


print("max no is ",z(a,b))
