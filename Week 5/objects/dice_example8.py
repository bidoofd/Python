
#Now we add color to our die and allow us to change the color
from die3 import Die

#create a 6(default) sides die with a default color
die1 = Die()

#create a 8 sides die with a blue color
die2 = Die(8,color='Blue')

#create a 20 sided die with a green color
die3 = Die(20)
die3.set_color('Green')


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




