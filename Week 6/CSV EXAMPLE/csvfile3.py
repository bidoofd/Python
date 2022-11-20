import csv
filename = "C:/Users/Tran/Desktop/coding/python/Week 6/CSV EXAMPLE/green.csv"
with open(filename) as file:
	data_from_file = csv.reader(file)
	header_row = next(data_from_file)
	
	for index,column_header in enumerate(header_row):
	#enumerate gives us the index number of the list
		print(index,column_header)
		
	