
from die4 import Die


die1 = Die()
print(die1.cup)
die2 = Die(8,color='Blue')
#notice I still use die1!!!!!
print(die1.cup)
die3 = Die(20)
die3.set_color('Green')
print(die1.cup)

#show_dice()
print("die1 = "+str((die1.faces())))
die1.roll()
print("die1 = "+str((die1.faces())))
print("die2 = "+str((die2.faces())))
die2.roll()
print("die2 = "+str((die2.faces())))
print("die3 = "+str((die3.faces())))
die3.roll()
print("die3 = "+str((die3.faces())))

print(die1.see_color())
print(die2.see_color())
print(die3.see_color())

bag_o_dice = {}

bag_o_dice[1] = die1
bag_o_dice[2] = die2
bag_o_dice[3] = die3

#wont work
print(bag_o_dice)
#wont work
print(bag_o_dice[2])

#will work!!!!
print(bag_o_dice[2].see_color())

#wont work
for num in range(0,len(bag_o_dice)):
	print (bag_o_dice[num+1].see_color())



