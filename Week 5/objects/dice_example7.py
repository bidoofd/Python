
from die2 import Die

	
# Create a D6.

die1 = Die()
die2 = Die(20)
for a in range(0,10):
	#notice we doll the die, but don't store the result anywhere!
	die1.roll()
	die2.roll()
	#but we can still see the result.  Our die now has a face property!
	print (die1.face,die2.face)
# we can also check the number of sides of that die
print("die1 has "+ str(die1.sides())+ " sides")
print("die2 has "+ str(die2.sides())+ " sides")

#now we have a set of more realistic dice
