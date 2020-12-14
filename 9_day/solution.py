import os

path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

data = []

for i in content:
    data.append(int(i))
    
#part 1 731031916
pre = 25

for i in range(pre, len(data)):
    combo = ""
    for j in range(i - pre, i):
        for k in range(j+1, i):
            if data[j]+data[k] == data[i]:
                # print(data[j], data[k], data[i])
                combo = "ok"
                break
    if combo == "":
        print(data[i])
        
#part 2

for i in range(len(data)):
    tot = [data[i]]
    for j in range(i + 1, len(data)):
        tot.append(data[j])
        if sum(tot) == 731031916:
            print(min(tot) + max(tot))
            break