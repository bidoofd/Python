# For this assignment you are to create three graphs using Python and the Matplotlib library.
# The first graph should be a line graph of average High temperatures for each month in a given city (not Pittsburgh).  You can find this data using Wikipedia (yes, it is OK to use Wikipedia).  Give your graph a title, label the X and Y axis and the tick marks on the X axis
# The second graph should be a scatter plot of the average temperature vs the average rainfall each month on your same city.  Again, label the graph.
# The third graph should be a pie chart showing the different categories of grades in this class and their relative percentage of the final grade.  The Project slice should be the only slice exploded from the rest of the pie.
 
# Submit the .py code and screen captures of the three graphs.
# HINT:  Here is a link to the https://en.wikipedia.org/wiki/Pittsburgh#Climate showing the climate data.  There is similar data for many other cities around the world.

import matplotlib.pyplot as graph

# Data for graphing. Source from https://www.ncei.noaa.gov/
tempData = [9,10,14,20,25,28,32,33,29,23,18,12]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "Septemper", "October", "November", "December"]
rainData = [38.9,73.3,101.1,128.3,126.2,194.9,159.9,108.9,154.8,148.3,82.3,56.9]

# Plotting temperature data
graph.plot(tempData)

# Labelling title and axes
graph.title("Average High Temperature in Osaka, Japan")
graph.xlabel("Months")
graph.ylabel("Temperature (in Celsius)")

# Adjusting label size of x axis
graph.tick_params(axis= "x", labelsize = 5)

# Plotting a line for the temperature data
graph.plot(months, tempData, color = "black", label = "Temperature")

#Showing legend and graph
graph.legend()
graph.show()

# Setting up scatter plot
graph.scatter(tempData, rainData)

# Labelling title and axes of plot
graph.title("Average High Temperature vs. Average rainfall in Osaka, Japan")
graph.xlabel("Temperature (in Celsius)")
graph.ylabel("Rainfall (in millimeters)")
graph.tick_params(axis= "both", labelsize = 14)

# Shows graph
graph.show()

# Data from syllabus
gradeData = [50,20,10,20]
hwData = ("Projects", "THE PROJECT", "Quiz", "Exam")

# Exploding "THE PROJECT" portion
explode = (0,0.5,0,0)

# Shows chart
fig1,ax1 = graph.subplots()
ax1.pie(gradeData, explode = explode,labels = hwData, startangle=45)
ax1.axis("equal") 
graph.show()	
