import matplotlib.pyplot as graph

data = [10,15,13,17,20,33,12]
days = ["10/1","10/2","10/3","10/4","10/5","10/6","10/7"]
data2 = [77,81,83,65,62,76,78]
data3 = [23,24,25,43,22,35,43]
graph.title("Average Wind Speed",fontsize = 14)
graph.xlabel("October",fontsize = 14)
graph.ylabel("MPH",fontsize = 14)
graph.tick_params(axis='both',labelsize = 14 )

graph.plot(days,data, color="black", label = "wind speed")
graph.plot(days,data2, color="green", label = "Temperature")
graph.plot(days,data3, color="blue", label = "humidity")
graph.legend()
graph.show()