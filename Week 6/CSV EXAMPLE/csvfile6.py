import csv
import matplotlib.pyplot as plt
filename = "C:/Users/draus/Desktop/Spring_2020b/Week6/files/Green.csv"
with open(filename) as file:
	data_from_file = csv.reader(file)
	header_row = next(data_from_file)
	

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
	print(trip_type)

labels = ('Credit card', 'Cash', 'No charge', 'Dispute', 'Unknown', 'Voided trip')
#sizes = [15, 30, 45, 10]
#explode = (0, 0, 0.1, 0.4,0.7,0.10)  
explode = (0, 0, 0.3, 0.6,0.9,0.12) 
fig1,ax1 = plt.subplots()
#fig = the entire plot
#axis aere the individual pie pieces
ax1.pie(trip_type, explode = explode,labels = labels, autopct='%1.1f%%', shadow=True, startangle=45)
#ax1.pie(trip_type, labels = labels, autopct='%1.1f%%', shadow=True, startangle=45)

ax1.axis('equal') 
plt.savefig('myplot')
plt.show()				