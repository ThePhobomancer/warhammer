#!usr/bin/env python
#This picks a career and gives skill and characteristic advances

import random
#Creates a matrix and sets each line to the first career level
career_line = [[]]

with open("careers_basic.txt", "r") as file:
    for line in file:
        career_line.append(line.strip().split(","))
        #print(career_line)

del career_line[0]


random_career = career_line[random.randint(0, len(career_line)-1)]
print("Career: ", random_career[0])
for i in range(1,9):
    print("Skill: ", random_career[i], "  +5")
for i in range(9,13):
    print("Talents: ", random_career[i])