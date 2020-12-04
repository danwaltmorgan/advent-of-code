import os
path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

list = []

for line in content:
    list.append(int(line))
    
#Part 1    
#539851
#Find two numbers that add up to 2020    
for i in list:
    for j in list:
        if (i + j == 2020):
            print(i,j, i* j)

#Part 2
#212481360
#Find 3 numbers that add up to 2020
for i in list:
    for j in list:
        for k in list:
            if (i + j + k == 2020):
                print(i,j,k, i * j * k)