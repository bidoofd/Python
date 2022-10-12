import json

filename = 'C:/Users/draus/Desktop/Spring_2020b/Week6/Chapter_10/numbers.json'
with open(filename) as file_object:
    numbers = json.load(file_object)
    
print(numbers)

for a in numbers:
	print(a)
