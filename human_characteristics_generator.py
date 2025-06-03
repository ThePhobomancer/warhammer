#!/usr/bin/env python
import random

human = []
for i in range(0,10):
    human.append(i)
    human[i] = 20 + random.randint(1,10) + random.randint(1,10)
print(human)
print("WS",human[0],"|BS",human[1],"|S",human[2],"|T",human[3],"|I",human[4],"|Ag",human[5],"|Dex",human[6],"|Int",human[7],"|WP",human[8],"|Fel",human[9])