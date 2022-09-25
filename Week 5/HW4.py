# For this assignment you are to create three graphs using Python and the Matplotlib library.
# The first graph should be a line graph of average High temperatures for each month in a given city (not Pittsburgh).  You can find this data using Wikipedia (yes, it is OK to use Wikipedia).  Give your graph a title, label the X and Y axis and the tick marks on the X axis
# The second graph should be a scatter plot of the average temperature vs the average rainfall each month on your same city.  Again, label the graph.
# The third graph should be a pie chart showing the different categories of grades in this class and their relative percentage of the final grade.  The “Project: slice should be the only slice exploded from the rest of the pie.
 
# Submit the .py code and screen captures of the three graphs.
# HINT:  Here is a link to the https://en.wikipedia.org/wiki/Pittsburgh#Climate showing the climate data.  There is similar data for many other cities around the world.

import matplotlib.pyplot as graph

highTemp = [9,10,14,20,25,28,32,33,29,23,18,12]
months = ["January", "February", "March", "April", "May", "June", "July," "August", "September", "October", "November", "December"]

graph.title("Average High Temperature in Osaka Japan")
graph.plot(months, highTemp, color = "black", label = "Temperature")