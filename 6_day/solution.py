import os

path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

file.close()

data = []

group = ""
for i in content:
    if i != '\n':
        group += i + " "
    else:
        data.append(group)
        group = ""
data.append(group)

#Part 1 6587
total = 0
for i in data:
    total += len(set(i))
    
print(total)

#Part 2

data_2 = []
group_2 = []
for i in content:
    if i != '\n':
        group_2.append(i.strip("\n"))
    else:
        data_2.append(group_2)
        group_2 = []
data_2.append(group_2)

#3235
total_2 = 0

for i in data_2:
    
    group_tot = 0
    g_set = set(i[0])
    
    for j in g_set:
        tot = 0
        group_len = len(i)
        for k in i:
            if j in k:
                tot += 1
        if tot == group_len:
            group_tot += 1
    total_2 += group_tot
print(total_2)