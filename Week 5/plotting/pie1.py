import matplotlib.pyplot as plt
trip_type = [40,50,22,5,2,7]
labels = ('Credit card', 'Cash', 'No charge', 'Dispute', 'Unknown', 'Voided trip')
#sizes = [15, 30, 45, 10]
explode = (0, 0, 0.0, 0.0,0.4,0.5)  
fig1,ax1 = plt.subplots()
#fig = the entire plot
#axis aere the individual pie pieces
ax1.pie(trip_type, explode = explode,labels = labels, autopct='%1.1f%%', shadow=True, startangle=45)
ax1.axis('equal') 

plt.show()				