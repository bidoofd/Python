import csv
filename = "C:/Users/draus/Desktop/Spring_2020b/Week6/files/people.csv"
with open(filename) as file:
	data_from_file = csv.reader(file)
#read in the first row of data from the CSV file makign a list
#from the items seperated by the commas
	header_row = next(data_from_file)
	for index,column_header in enumerate(header_row):
		print(index,column_header)
		
	see = input("What column do you want to see?")
	see = int(see)
	column = []
    #you can also loop thorugh the entire data file
	for row in data_from_file:
		temp = row[see]
		print(temp)
	