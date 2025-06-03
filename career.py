#!usr/bin/env python
#This picks a career and gives skill and characteristic advances

#Creates a matrix and sets each line to the first career level
career_line = [[]]

with open("careers_basic.txt", "r") as file:
    for line in file:
        career_line.append(line.strip().split(","))
        #print(career_line)

del career_line[0]

for i in range(8):
    print(career_line[i])