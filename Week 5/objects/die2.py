from random import randint

class Die():

#now our object not only gives a random number, but has properties (number of sides AND a face)
	def __init__(self, num_sides=6,face=1,color = 'Red'):
		self.num_sides = num_sides
		self.face = face
		
	def roll(self):
		self.face = randint(1, self.num_sides)
		return self.face

	def sides(self):
		return self.num_sides

	def faces(self):
		return self.face

		