import os

path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

data = []

for i in content:
    data.append(i.strip('\n'))
    
print(data)

#Part 1 1x3 slope: 232
total = 0
index = 0
for i in range(len(data)):
    if data[i][index] == "#":
        total += 1
    index += 3
    if index >= len(data[i]):
        index = index - len(data[i])

print(total)

def slope(d,r):
    tot = 0
    idx = 0
    for i in range(0,len(data),d):
        if data[i][idx] == "#":
            tot += 1
        idx += r
        if idx >= len(data[i]):
            idx = idx - len(data[i])
            
    return tot

print(slope(1,1) * slope(1,3) * slope(1,5) * slope(1,7) * slope(2,1))

