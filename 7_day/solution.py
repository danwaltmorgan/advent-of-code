import os
import re

path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

data = []

for i in content:
    data.append(i)
    
bags = ["shiny gold"]

#Part 1 155
while True:
    acc = len(set(bags))
    test = acc
    for i in data:
        regex = re.compile(r'(.+) bags contain (.+)')
        bag = regex.search(i)
        for j in bags:
            if j in bag.group(2):
                bags.append(bag.group(1))
                acc += 1
    af = len(set(bags))
    if af == test:
        break
    

#Part 2 54803   

bags2 = ["shiny gold"]

for i in bags2:
    for j in data:
        regex = re.compile(r'(.+) bags contain (.+)')
        bag = regex.search(j)
        if i in bag.group(1):
            inside = bag.group(2)
            rules = re.compile(r'(\d+) (\w+ \w+)')
            num = rules.findall(j)
            for k in num: 
                for l in range(int(k[0])):
                    bags2.append(k[1])
                    print(k[1])
                    
print(len(bags2))
                
