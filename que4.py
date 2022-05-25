n = int(input("ente the no of strings\n"))

li = []

for i in range(n):
    li.append(input())


print(list(map(lambda x: len(x), li)))
