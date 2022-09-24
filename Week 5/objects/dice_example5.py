from die import Die

# Create a D6 object flexible enough to have different number of sides

die1 = Die(6)
die2 = Die(20)
for a in range(0,10):
	roll = die1.roll()
	roll2 = die2.roll()
	print (roll,roll2)



#but still not a good dice object