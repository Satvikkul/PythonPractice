# So the scenario is we have a character who has some health.
# Let's say he has 45 points.
# We imagine that this character has walked over a health potion and the health potion magically increases
# their health by a random amount.
# I guess in this case quite a lot but the game also has three difficulty settings easy medium and hard
# depending on what difficulty is selected.
# The amount of health that the person gets from the potion will change and this will be less on higher difficulties.

import random

health = 50

#difficulty = 1(easy), 2(medium), 3(hard)
difficulty = 1

potionHealth = int(random.randint(25, 50) / difficulty)
health = health + potionHealth
print(health)


