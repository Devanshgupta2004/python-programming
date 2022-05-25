# d = {}

# print('enter the size of the dictionary')

# n = int(input())

# for  i in range(n):
#     d[i] = input()


# print(d)


# d = {'aman' : 64, 'rahul' : 75, 'madhav' : 33, 'shashank' : 55}


# d1 = eval(input("Enter the dictionary\n"))

# for i in d1:
#     print("key = ",i, "value = ",d1[i])


# d = {'aman': 64, 'rahul': 75, 'madhav': 33, 'shashank': 55}

# max = 0

# for i in d:
#     if d[i] > max:
#         max = d[i]


# print('The highest score is', max)


# d = {'aman': 64, 'rahul': 75, 'madhav': 33, 'shashank': 55}

# name = ''                                                                           

# max = 0

# for i in d:
#     if d[i] > max:
#         max = d[i]
#         name = i


# print(name, 'scored the highest marks')


d = {'aman': [64, 45, 67], 'rahul': [75, 56, 35],
     'madhav': [33, 53, 98], 'shashank': [55, 33, 43]}

max = 0
name = ''

for i in d:
    if sum(d[i]) > max:
        max = sum(d[i])
        name = i


print(name)
