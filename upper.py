f=open("python.py","r")
x=f.read()
low=0
upp=0
for i in x:
    if i>="a" and i<="z":
        low=low+1
    elif i>="A" and i<="Z":
        upp=upp+1 
print(upp,low)
f.close()          