import re
import os


path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

data = []

for i in content:
    data.append(i)
    
total_1 = 0
total_2 = 0

for i in data:
    
    regex = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
    mo = regex.search(i)
    
    lower = int(mo.group(1))
    upper = int(mo.group(2))
    letter = mo.group(3)
    password = mo.group(4)
    
    test = re.compile(r'(%s)'%letter)
    policy = test.findall(password)

    #first password policy
    #542
    #Find passwords that constain same amount of letters as indicated
    length = len(policy)
    
    if (length >= lower and length <= upper):
        total_1 += 1
      
    #Second password policy
    #360
    #Find passwords that conatin letter at specified index
    if ((password[lower - 1] == letter and password[upper - 1] != letter) or 
        (password[lower - 1] != letter and password[upper - 1] == letter)):
        total_2 += 1
        
print(total_1, total_2)