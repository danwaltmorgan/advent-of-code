import os
import re

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
        
data.append(content[-1])        


credentials = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

#Part 1: 226

total = 0

for i in data:
    tot = 0
    for j in credentials:
        if j in i:
            tot += 1
    if tot == 7:
        total += 1
print(total)

#Part 2

val = []

for i in data:
    pas = {}
    for j in credentials:
        match = re.search(r"(%s):(#?\w+)"%j, i)
        if match:
            pas[match.group(1)] = match.group(2)
    val.append(pas)

test = 0
for i in val:
    tot = 0
    if ("byr" in i 
        and int(i["byr"])>=1920
        and int(i["byr"])<=2002):
        tot += 1
    if ("iyr" in i 
        and int(i["iyr"])>=2010
        and int(i["iyr"])<=2020):
        tot += 1
    if ("eyr" in i
        and int(i["eyr"])>=2020
        and int(i["eyr"])<=2030):
        tot += 1
    if ("hgt" in i):
        unit = re.search(r"(\d+)(\w{2})", i["hgt"])
        if unit:
            if unit.group(2) == "cm":
                if int(unit.group(1)) >= 150 and int(unit.group(1)) <=193:
                    tot += 1
            if unit.group(2) == "in":
                if int(unit.group(1)) >= 59 and int(unit.group(1)) <= 76:
                    tot += 1
    if ("hcl" in i):
        color = re.search(r"(#[0-9a-f]+)", i["hcl"])
        if color and len(color.group(1)) == 7:
            tot += 1
    if ("ecl" in i):
        ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        for j in ecl:
            if j in i["ecl"]:
                tot += 1
    if ("pid" in i and len(i["pid"]) == 9):
        tot += 1
       
    if tot == 7:
       test += 1 
    
    print(tot)
    
print(test)
print(total)