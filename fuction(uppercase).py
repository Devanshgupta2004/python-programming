def toUppercase(s):

    s2 = ""

    for i in s:
        if ord(i) >= 97 and ord(i) <= 123:
            s2 += chr(ord(i) - 32)
        else:
            s2 += i

    print(s2)


s = input("Enter the string\n")

toUppercase(s)
