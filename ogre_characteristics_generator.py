#!/use/bin/env python
## Generate Dwarven character characteristics. Due to hard coded
import random

ogre = []
for i in range(0,10):
    ogre.append(i)
    ogre[i] = 20 + random.randint(1,10) + random.randint(1,10)
#ogre[0] = ogre[0]
ogre[1] = ogre[1] -10
ogre[2] = ogre[2] +15
ogre[3] = ogre[3] +15
ogre[4] = ogre[4] -20
ogre[5] = ogre[5] -5
ogre[6] = ogre[6] -10
ogre[7] = ogre[7] -10
#ogre[8] = ogre[8]
ogre[9] = ogre[9] -10
#print(ogre)
print("WS",ogre[0],"|BS",ogre[1],"|S",ogre[2],"|T",ogre[3],"|I",ogre[4],"|Ag",ogre[5],"|Dex",ogre[6],"|Int",ogre[7],"|WP",ogre[8],"|Fel",ogre[9])