#!/usr/bin/env python
##Generate a number of objects in a room for a medieval roleplaying game.

import random

room_furniture = []
with open('room_furniture.txt', 'r') as file_furniture:
    for line in file_furniture:
        room_furniture.append(line.strip())  # strip() removes newline characters
##print(room_furniture) ##The file is read properly into the list

room_loot = []
with open('room_loot.txt', 'r') as file_loot:
    for line in file_loot:
        room_loot.append(line.strip())  # strip() removes newline characters
##print(room_loot[0]) ##The file is read properly into the list

room_objects = []
with open('room_objects.txt', 'r') as file_objects:
    for line in file_objects:
        room_objects.append(line.strip())  # strip() removes newline characters
##print(room_objects[0]) ##The file is read properly into the list

room_features = []
with open('room_features.txt', 'r') as file_features:
    for line in file_features:
        room_features.append(line.strip())  # strip() removes newline characters

room_type = []
with open('room_type.txt', 'r') as file_roomtype:
    for line in file_roomtype:
        room_type.append(line.strip())  # strip() removes newline characters


##Rooms will have a random number of objects, loot and furniture items. Each element will be placed into a room list.
room_contents = []
for i in range(0,random.randint(1,2)):
    randomelement = random.choice(room_type)
    room_contents.append(randomelement)
for i in range(0,random.randint(1,5)):
    randomelement = random.choice(room_features)
    room_contents.append(randomelement)
for i in range(0,random.randint(1,5)):
    randomelement = random.choice(room_furniture)
    room_contents.append(randomelement)
for i in range(0,random.randint(1,3)):
    randomelement = random.choice(room_loot)
    room_contents.append(randomelement)
for i in range(0,random.randint(1,7)):
    randomelement = random.choice(room_objects)
    room_contents.append(randomelement)

for item in room_contents:
    print(item)
#prints room contents with each element being on a new line