#!usr/bin/env python
# This creates a hallway description and features

import random

# The hallway should have a style, objects, features, length, turns and doorways

# Hall length determines number of doorways
size = random.randint(1,10)
hall_length = size * 10
doorways = random.randint(0,size) + 1

hall_shape = "The hall "
hall_shape_type = random.randint(1,10)

if hall_shape_type == 10:
    hall_shape += "is curved"
elif hall_shape_type == 9:
    hall_shape += "is cross shaped"
elif hall_shape_type == 8:
    hall_shape += "is T shaped"
elif hall_shape_type == 7 | hall_shape_type == 6:
    hall_shape += "turns right"
elif hall_shape_type == 5 | hall_shape_type == 4:
    hall_shape += "turns left"
elif hall_shape_type <= 4:
    hall_shape += "is straight"



hall_style = []
with open('hall_style.txt', 'r') as file_style:
    for line in file_style:
        hall_style.append(line.strip())  # strip() removes newline characters
##print(hall_style) ##The file is read properly into the list

hall_objects = []
with open('hall_objs.txt', 'r') as file_objects:
    for line in file_objects:
        hall_objects.append(line.strip())  # strip() removes newline characters
##print(hall_objects[0]) ##The file is read properly into the list

hall_description = random.choice(hall_style)

hall_objs = []
for i in range(0,random.randint(1,7)):
    randomelement = random.choice(hall_objects)
    hall_objs.append(randomelement)


print("The hallway is " + hall_description)
print("The hallway is ", hall_length, " feet long, with ", doorways, " doorways")
print(hall_shape)
print("The hall has:")
for item in hall_objs:
    print("  ", item)