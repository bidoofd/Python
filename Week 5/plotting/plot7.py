import matplotlib.pyplot as graph

data = [10,15,13,17,20,33,12]
days = ["10/1","10/2","10/3","10/4","10/5","10/6","10/7"]
data2 = [350,370,360,360,330,350,350]
graph.title("Stock Proces",fontsize = 14)
graph.xlabel("October",fontsize = 14)
graph.ylabel("Dollar per share",fontsize = 14)
graph.tick_params(axis='both',labelsize = 14 )

graph.plot(days,data, color="red", label = "Sprockets Inc.")
graph.plot(days,data2, color="purple", label = "Bedrock Mining")
graph.legend()
graph.savefig('d:/python/Week9/WindSpeed.png')
graph.show()