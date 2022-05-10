import hashlib

flag=0
counter=0

pass_hash=input("file name:")

wordlist=input("file name:")
try:
    pass_file=open(wordlist,"r")

except:
    print("no file found")
    quit()

for i in pass_file:
    enc_wrd=word.encode('utf-8')
    digest=hashlib.md5(enc_wrd.strip()).hexdigest()

   # print(word)
    #print(digest)
    #rint(pass_hash)

    if digest== pass_hash:
        print("password has been found")
        print("password is "+ word)
        flag=1
        break

if flag==0:
    print("password is not found in list")    

#we use this to crack the password but we need a file which have some comman passwords hackers are also do that 