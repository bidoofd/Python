from random import randint

class Die():
	cup = 0

	def __init__(self, num_sides=6,face=1,color = 'Red'):
		self.num_sides = num_sides
		self.face = face
		self.color = color
		Die.cup = Die.cup+1
		
	def roll(self):
		self.face = randint(1, self.num_sides)
		return self.face

	def see_color(self):
		return self.color

	def sides(self):
		return self.num_sides

	def faces(self):
		return self.face
		
	def set_color(self,new_color='Red'):
		self.color = new_color
		