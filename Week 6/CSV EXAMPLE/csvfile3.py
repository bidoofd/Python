import csv
filename = "C:/Users/draus/Desktop/Spring_2020b/Week6/files/green.csv"
with open(filename) as file:
	data_from_file = csv.reader(file)
	header_row = next(data_from_file)
	
	for index,column_header in enumerate(header_row):
	#enumerate gives us the index number of the list
		print(index,column_header)
		
	