import time
from turtle import *
AI= Turtle()
s=57
m=59
h=23
while True:
    AI.clear()
    AI.write(str(h).zfill(2) + "h:" + str(m).zfill(2) + "min:" + str(s).zfill(2)+"sec", font=("arial",20,"bold"))
    s=s+1
    time.sleep(1)
    if s==60:
        s=0
        m=m+1
    if m==60:
        m=0
        h=h+1
    if h == 24 :
        h=0

