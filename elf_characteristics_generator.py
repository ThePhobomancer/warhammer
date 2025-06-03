#!/use/bin/env python
## Generate Elf character characteristics. Due to hard coded
import random

elf = []
for i in range(0,10):
    elf.append(i)
    elf[i] = 20 + random.randint(1,10) + random.randint(1,10)
elf[0] = elf[0] +10
elf[1] = elf[1] +10
elf[4] = elf[4] +20
elf[5] = elf[5] +10
elf[6] = elf[6] +10
elf[7] = elf[7] +10
elf[8] = elf[8] +10
print(elf)
print("WS",elf[0],"|BS",elf[1],"|S",elf[2],"|T",elf[3],"|I",elf[4],"|Ag",elf[5],"|Dex",elf[6],"|Int",elf[7],"|WP",elf[8],"|Fel",elf[9])