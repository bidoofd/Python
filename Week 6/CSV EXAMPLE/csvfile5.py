import csv
filename = "C:/Users/draus/Desktop/Spring_2020b/Week6/files/Green.csv"
with open(filename) as file:
	data_from_file = csv.reader(file)
	header_row = next(data_from_file)
	
	
	print('Lets look at the trip type column and do some counting...')
	column = []
	trip_type = [0,0,0,0,0,0]
	for row in data_from_file:
		temp = int(row[17])
		if temp == 1:
			trip_type[0] = trip_type[0] +1
		elif temp == 2:
			trip_type[1] = trip_type[1] +1		
		elif temp == 3:
			trip_type[2] = trip_type[2] +1
		elif temp == 4:
			trip_type[3] = trip_type[3] +1
		elif temp == 5:
			trip_type[4] = trip_type[4] +1
		elif temp == 6:
			trip_type[5] = trip_type[5] +1

			
trip_catagories = ['Credit card','Cash','No charge','Dispute','Unknown','Voided trip']
for number in range(0,5): 
    print(trip_catagories[number] + ' = '+ str(trip_type[number]))