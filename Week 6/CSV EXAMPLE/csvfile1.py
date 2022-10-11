#import the CSV file library
import csv

#set a vareiable filename to the loaction and filenmae
filename = "C:/Users/draus/Desktop/Spring_2020b/Week6/files/green.csv"

#The 'with' command allows us to encapsulate the commands that you execute when the
#file is open and automatically closes the file when finished
#the open command opens the file for reading or writing and gies it a handle to use 
#in the code
with open(filename) as file:
    
    #This command creates a Python object to link to the file
	data_from_file = csv.reader(file)
    
    #The next command reads a line of data from the file that 
	header_row = next(data_from_file)
    
    #we print the first line of code
	print(header_row)
	