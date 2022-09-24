
from die2 import Die

	
# Create a D6.

die1 = Die()
for a in range(0,10):
	#notice we doll the die, but don't store the result anywhere!
	die1.roll()
	#but we can still see the result.  Our die now has a face property!
	print (die1.face)
# we can also check the number of sides of that die
print("die1 has "+ str(die1.sides())+ " sides")