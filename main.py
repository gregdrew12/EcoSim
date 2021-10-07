import settings
from creature import *
from food import *

for i in range(1):
    settings.init()
    #for i in settings.map:
        #print(i)
    settings.creature.sim()
    #settings.creature = Creature()