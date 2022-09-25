# Using matplotlib, make a few line graphs.
# Some guidance.
#   Lable the graph
#   lable the axis
#   have at least 10 data points
#   have at least two lines
#   change the color of the lines
#   Maybe if you feel motivated, ask the uer to enter the values and then graph them.

import matplotlib.pyplot as graph

tempData = [10,30,25,60,80,67,32,45,69,10]
days = ["10/1", "10/2", "10/3", "10/4", "10/5", "10/6", "10/7", "10/8", "10/9", "10/10"]
rainData = [1,3,5,2,3,4,2,5,1,2]
graph.plot(tempData)
graph.title("")
graph.xlabel("October")
graph.ylabel("Temperature")
graph.plot(days, tempData, color = "black", label = "Temperature")
graph.plot(days, rainData, color = "blue", label = "Rain Depth")
graph.legend()
graph.show()

