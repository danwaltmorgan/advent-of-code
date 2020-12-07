import os


path = os.path.dirname(os.path.realpath(__file__))

file = open(os.path.join(path, "input.txt"), "r")

content = file.readlines()

data = []

for i in content:
    data.append(i)
    

test = "BBFFBBFRLL"

highest = 0

all_id = []

for i in data:
    #not inclusive
    row_max = 128
    row_min = 0
    col_max = 8
    col_min = 0
    
    for j in i:
        if j == "F":
            row_max = (row_max + row_min) / 2
        if j == "B":
            row_min = (row_max + row_min) / 2
        if j == "R":
            col_min = (col_max + col_min) / 2
        if j == "L":
            col_max = (col_max + col_min) / 2
    
    row = row_min
    col = col_min
    
    seat_id = (row * 8) + col
    
    if seat_id > highest:
        highest = seat_id
        
    all_id.append(seat_id)
    
print(highest)

#Part 2: 615

all_id = sorted(all_id)

solutions = []

for i in range(8,len(all_id) - 8):
    if all_id[i + 1] != all_id[i] + 1 or all_id[i - 1] != all_id[i] - 1:
        print(all_id[i])
    