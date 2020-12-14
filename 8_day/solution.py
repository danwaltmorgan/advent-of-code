import os
import re

path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

data = []

for i in content:
    data.append(i)
    
#Part 1 2014
# =============================================================================
# 
# test = [0] * len(data)
# 
# idx = 0
# acc = 0
# 
# regex = re.compile(r'(\w+) (.+)')
# 
# while True:    
#     test[idx] += 1
#     
#     if test[idx] > 1:
#         break
#     rule = regex.search(data[idx])
#     if rule.group(1) == "nop":
#         idx += 1
#     
#     if rule.group(1) == "acc":
#         acc += int(rule.group(2))
#         idx += 1
#     
#     if rule.group(1) == "jmp":
#         idx += int(rule.group(2))
#         
#     
# print(acc)
#      
# =============================================================================

#Part 2 2251

for i in range(len(data)):
    alt = data[:]
    regex = re.compile(r'(\w+) (.+)')
    rule = regex.search(alt[i])
    
    if rule.group(1) == "nop":
        alt[i] = "jmp " + rule.group(2)
    if rule.group(1) == "jmp":
        alt[i] = "nop " + rule.group(2)

    test = [0] * len(alt)
    
    acc = 0 
    idx = 0
    
    while True:    
        test[idx] += 1
        
        if test[idx] > 1 or idx < 0:
            break
        
        ma = regex.search(alt[idx])
        
        if ma.group(1) == "nop":
            idx += 1
        
        if ma.group(1) == "acc":
            acc += int(ma.group(2))
            if idx != len(alt) - 1:
                idx += 1
        
        if ma.group(1) == "jmp":
            idx += int(ma.group(2))
        if test[len(alt) - 1] == 1:
            print(acc)
            
    
