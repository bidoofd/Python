import matplotlib.pyplot as graph

data = [10,15,13,17,20,33,12]
days = ["10/1","10/2","10/3","10/4","10/5","10/6","10/7"]
graph.title("Average Wind Speed")
graph.xlabel("October")
graph.ylabel("MPH")
graph.plot(days,data)
graph.show()
