# Create a D6 function.
from random import randint
def roll(item):
	item = randint(1, 6)
	return(item)
die1 = 0
for a in range(0,10):
	die1 = roll(die1)
	print (die1)


