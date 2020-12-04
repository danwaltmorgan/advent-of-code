import os
path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

list = []

for line in content:
    list.append(int(line))
    
    
#539851    
for i in list:
    for j in list:
        if (i + j == 2020):
            print(i,j, i* j)

#212481360
for i in list:
    for j in list:
        for k in list:
            if (i + j + k == 2020):
                print(i,j,k, i * j * k)