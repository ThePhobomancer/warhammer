#!usr/bin/env python
#This picks a career and gives skill and characteristic advances

import random
#Creates a matrix and sets each line to the first career level
career_line = [[]]

#The Career_basics file has the format: 
#Career Name 1, Career Title, Status, Income skill, skill, skill, skill, skill, skill, skill, skill, talent, talent, talent, talent
#This provides all the core information of the first career level in these skills. Except for characteristics.
with open("careers_basic.txt", "r") as file:
    for line in file:
        career_line.append(line.strip().split(","))
        #print(career_line)

del career_line[0]


random_career = career_line[random.randint(0, len(career_line)-1)]
print("Career: ", random_career[0], "Title: ", random_career[1], "Status: ", random_career[2])
print("Career Skill: ", random_career[3], "  +10")
for i in range(4,11):
    print("Skill: ", random_career[i], "  +5")
for i in range(11,15):
    print("Talents: ", random_career[i])