import os

path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

data = []

for i in content:
    data.append(int(i))
    
data.append(0)
data.append(max(data) + 3)
    
data.sort()

# Part 1 2516
ones = 0
threes = 0

for i in range(len(data) - 1):
    dif = data[i + 1] - data[i]
    if dif == 1:
        ones += 1
    if dif == 3:
        threes += 1
    
print(ones, threes) 

#Part 2 296196766695424

count = 0

    
dif = []
for i in range(len(data) - 1):
    dif.append(data[i + 1] - data[i])
print(dif)

temp = []
mult = []

for i in dif:
    if i != 3:
        temp.append(i)
    elif i == 3:
        if len(temp) > 3:
            mult.append((len(temp) - 1) * 2 + (len(temp) - 3))
        elif len(temp) > 1:
            mult.append((len(temp) - 1) * 2)
        temp = []
    
tot = 1
for i in mult:
    tot *= i
print(mult)
print(tot)




