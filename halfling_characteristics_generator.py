#!/usr/bin/env python
## Generate Halfing character characteristics. Due to hard coded
import random

halfling = []
for i in range(0,10):
    halfling.append(i)
    halfling[i] = 20 + random.randint(1,10) + random.randint(1,10)
halfling[0] = halfling[0] -10
halfling[1] = halfling[1] +10
halfling[2] = halfling[2] -10
halfling[6] = halfling[6] +10
halfling[8] = halfling[8] +10
halfling[9] = halfling[9] +10
#print(halfling)
print("WS",halfling[0],"|BS",halfling[1],"|S",halfling[2],"|T",halfling[3],"|I",halfling[4],"|Ag",halfling[5],"|Dex",halfling[6],"|Int",halfling[7],"|WP",halfling[8],"|Fel",halfling[9])