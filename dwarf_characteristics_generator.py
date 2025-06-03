#!/usr/bin/env python
## Generate Dwarven character characteristics. Due to hard coded
import random

dwarf = []
for i in range(0,10):
    dwarf.append(i)
    dwarf[i] = 20 + random.randint(1,10) + random.randint(1,10)
dwarf[0] = dwarf[0] +10
dwarf[3] = dwarf[3] +10
dwarf[5] = dwarf[5] -10
dwarf[6] = dwarf[6] +10
dwarf[8] = dwarf[8] +20
dwarf[9] = dwarf[9] -10
#print(dwarf)
print("WS",dwarf[0],"|BS",dwarf[1],"|S",dwarf[2],"|T",dwarf[3],"|I",dwarf[4],"|Ag",dwarf[5],"|Dex",dwarf[6],"|Int",dwarf[7],"|WP",dwarf[8],"|Fel",dwarf[9])