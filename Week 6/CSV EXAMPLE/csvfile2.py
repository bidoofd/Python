import csv
filename = "C:/Users/draus/Desktop/Spring_2020b/Week6/files/green.csv"


with open(filename) as file:
#open the file and set up reader object
    data_from_file = csv.reader(file)
    
    
#read the first row of data into a list variable called 'header_row' we are assuming it is a header row - remember this is NOT
#always the case
    header_row = next(data_from_file)



#go through the list
    for column_header in header_row:
        print(column_header)
    print('\n**********\n')
        
        
#read the next row of data       
    data_row = next(data_from_file)
    
    
#we can loop through ANY row in the csv file
    for column_header in data_row:
        print(column_header)