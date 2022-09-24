import matplotlib.pyplot as graph

data = [10,15,13,17,20,33,12]
days = [45,33,56,12,25,33,25]
graph.title("Wind Speed vs % Sunlight",fontsize = 14)
graph.xlabel("% Sunlight",fontsize = 14)
graph.ylabel("MPH",fontsize = 14)
graph.tick_params(axis='both',labelsize = 14)
graph.scatter(days,data,c='red',edgecolor='blue',s=100)
graph.show()