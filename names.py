#!/usr/bin/env python
import random

mens_list = []
with open('names_men.txt', 'r') as file_men:
    for line in file_men:
        mens_list.append(line.strip())  # strip() removes newline characters
##print(mens_list) ##The names are read properly into the list

random_name_men = random.choice(mens_list)
print(random_name_men)

womens_list = []
with open('names_women.txt', 'r') as file_women:
    for line in file_women:
        womens_list.append(line.strip())  # strip() removes newline characters

random_name_women = random.choice(womens_list)
print(random_name_women)