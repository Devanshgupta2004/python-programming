def allArmstrong(lb,ub):
    count = 0
    for i in range (lb,ub+1):
        no = lb
        while (lb>0):
            lb = lb//10
            count += 1

        while (no>0): 
            st += (no%10)**count


    





lb = int(input("Enter the lower limit\n"))
ub = int(input("Enter the upper limit\n"))
