import csv
filename = "C:/Users/draus/Desktop/Spring_2020b/Week6/files/Green.csv"
with open(filename) as file:
	data_from_file = csv.reader(file)
	header_row = next(data_from_file)
	
	for index,column_header in enumerate(header_row):
		print(index,column_header)
		
	see = input("What column do you want to see? ")
	see = int(see)
	column = []
	for row in data_from_file:
		print(row)
        