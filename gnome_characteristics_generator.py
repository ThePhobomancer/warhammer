#!/use/bin/env python
## Generate Dwarven character characteristics. Due to hard coded
import random

gnome = []
for i in range(0,10):
    gnome.append(i)
    gnome[i] = 20 + random.randint(1,10) + random.randint(1,10)
#gnome[0] = gnome[0]
gnome[1] = gnome[1] -10
gnome[2] = gnome[2] -10
gnome[3] = gnome[3] -5
gnome[4] = gnome[4] +10
gnome[5] = gnome[5] +10
gnome[6] = gnome[6] +10
gnome[7] = gnome[7] +10
gnome[8] = gnome[8] +20
gnome[9] = gnome[9] -5
#print(gnome)
print("WS",gnome[0],"|BS",gnome[1],"|S",gnome[2],"|T",gnome[3],"|I",gnome[4],"|Ag",gnome[5],"|Dex",gnome[6],"|Int",gnome[7],"|WP",gnome[8],"|Fel",gnome[9])