import csv
import json
import matplotlib.pyplot as plt

def findCount(fn, countList, rowNum, userNumList):
	#Opens file for reading
	count = 0
	with open(fn) as file:
		data_from_file = csv.reader(file)
		#Finds count values based on what is found
		#Such as strings and ints
		if len(userNumList) > 0:
			for row in data_from_file:
				for a in range(0,5):
					temp = row[rowNum]
					if(temp == str(userNumList[a])):
						countList[a] = countList[a] + 1
		else:
			for row in data_from_file:
				temp = row[rowNum]
				if(temp.isdigit() == True):
					temp = int(temp)
					if(temp > 0 and temp < 10):
						if(temp == 1):
							countList[0] = countList[0] +1
						elif (temp == 2):
							countList[1] = countList[1] +1		
						elif (temp == 3):
							countList[2] = countList[2] +1
						elif (temp == 4):
							countList[3] = countList[3] +1
						elif (temp == 5):
							countList[4] = countList[4] +1
						elif (temp == 6):
							countList[5] = countList[5] +1
					else:
						if temp >= 0 and temp <= 999:
							countList[0] = countList[0] +1
						elif temp >= 1000 and temp <= 1999:
							countList[1] = countList[1] +1		
						elif temp >= 2000 and temp <= 2999:
							countList[2] = countList[2] +1
						elif temp >= 3000 and temp <= 3999:
							countList[3] = countList[3] +1
						elif temp >= 4000 and temp <= 4999:
							countList[4] = countList[4] +1
						elif temp >= 5000 and temp <= 5999:
							countList[5] = countList[5] +1
						elif temp >= 6000 and temp <= 6999:
							countList[6] = countList[6] +1
						elif temp >= 7000 and temp <= 7999:
							countList[7] = countList[7] +1
						elif temp >= 8000 and temp <= 8999:
							countList[8] = countList[8] +1
						elif temp >= 9000 and temp <= 9999:
							countList[9] = countList[9] +1
				else:
					if(chr(ord(temp[0:1])) == "1"):
						if(temp[1:2]  == "A"):
							countList[1] = countList[1] + 1
						elif(temp[1:2]  == "B"):
							countList[2] = countList[2] + 1
						elif(temp[1:2]  == "C"):
							countList[3] = countList[3] + 1
						elif(temp[1:2]  == "M"):
							countList[4] = countList[4] + 1
					elif(chr(ord(temp[0:1])) == "2"):
						if(temp[1:2]  == "A"):
							countList[5] = countList[5] + 1
						elif(temp[1:2]  == "B"):
							countList[6] = countList[6] + 1
						elif(temp[1:2]  == "C"):
							countList[7] = countList[7] + 1
						elif(temp[1:2]  == "M"):
							countList[8] = countList[8] + 1
					elif(chr(ord(temp[0:1])) == "3"):
						if(temp[1:2]  == "A"):
							countList[9] = countList[9] + 1
						elif(temp[1:2]  == "B"):
							countList[10] = countList[10] + 1
						elif(temp[1:2]  == "C"):
							countList[11] = countList[11] + 1
						elif(temp[1:2]  == "M"):
							countList[12] = countList[12] + 1
					elif(chr(ord(temp[0:1])) == "4"):
						if(temp[1:2]  == "A"):
							countList[13] = countList[13] + 1
						elif(temp[1:2]  == "B"):
							countList[14] = countList[14] + 1
						elif(temp[1:2]  == "C"):
							countList[15] = countList[15] + 1
						elif(temp[1:2]  == "M"):
							countList[16] = countList[16] + 1
					elif(chr(ord(temp[0:1])) == "5"):
						if(temp[1:2]  == "A"):
							countList[17] = countList[17] + 1
						elif(temp[1:2]  == "B"):
							countList[18] = countList[18] + 1
						elif(temp[1:2]  == "C"):
							countList[19] = countList[19] + 1
						elif(temp[1:2]  == "M"):
							countList[20] = countList[20] + 1
					elif(chr(ord(temp[0:1])) == "6"):
						if(temp[1:2]  == "A"):
							countList[21] = countList[21] + 1
						elif(temp[1:2]  == "B"):
							countList[22] = countList[22] + 1
						elif(temp[1:2]  == "C"):
							countList[23] = countList[23] + 1
						elif(temp[1:2]  == "M"):
							countList[24] = countList[24] + 1
					elif(temp[0:1] == " "):
						countList[0] = countList[0] + 1           
				
	#returns the countlist
	return countList
					
#Function to display crime report
def displayCrimeReport():
	#Variables declared
	lnCode = {}
	
	oldncic_code_count = [0,0,0,0,0,0,0,0,0,0]
	olddistrict_count = [0,0,0,0,0,0]
	oldbeat_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	empty = []
	fJSON = "/Users/trando/Desktop/coding/python/Python/Week 6/PROJECT1/January.json"
	filename = "/Users/trando/Desktop/coding/python/Python/Week 6/PROJECT1/crime.csv"
	#Using the findCount function to find the count of respective name
	ncic_code_count = findCount(filename, oldncic_code_count, 6, empty)
	district_count = findCount(filename, olddistrict_count, 2, empty)
	beat_count = findCount(filename, oldbeat_count, 3, empty)

	#Opening JSON file
	try:
		with open(fJSON) as json_file:  
			lnCode = json.load(json_file)
	except  FileNotFoundError:
	# if no old data found, inform th euser, but no other action made
		print ("No old data to load.\n")
		input("Press Enter to continue...")
		# Set a flag to indicate that polling is active.
	polling_active = True
		
	#temporary variables for text purposes
	var2 = 0
	var3 = 999
	
	#Adding counts to a string, then the string is added to a respective key in the dictionary
	while polling_active:
		#For loops top concatenate strings
		for a in range(0,10):
			text = ("NCIC Code Count from range " + str(var2) + "-" + str(var3) + ": ")
			lnCode['NCIC CODE'].append({
				text: str(ncic_code_count[a])
			})
			
			#temp variables used for string range. (Adds 1000 for each range)
			var2 = var2 + 1000
			var3 = var3 + 1000  
			
		for b in range(0,6):
			text = ("Disctrict " + str(b) + " Count: " )
			lnCode['DISTRICT'].append({
				text: str(district_count[b])
			})


		#more temporary variables
		count = 1
		count2 = 0
		tempList = ['A', 'B', 'C', 'M']
		numList = [0,1,2,3,4,5,6]
		for c in range(0,25):
			if(c == 0):
				text = ("Beat 0 Count: ")
				lnCode['BEAT'].append({
					text: str(beat_count[c])
				})
			else:
				text = ("Beat " + str(numList[count]) + tempList[count2] + " Count: ")
				lnCode['BEAT'].append({
					text: str(beat_count[c])
				})
	#Counter variables for the lists for the JSON
				count2 = count2 + 1
			if(count2 == 4):
				count2 = 0
				count = count + 1
			if(count == 7):
				count = 1
		polling_active = False


	#Puts the dictionary in the JSON file
	polling_active = True
	
	while polling_active:
		with open(fJSON, 'w') as file_object:
			json.dump(lnCode, file_object, indent = 4)
		polling_active = False
	
	#Prints out what was stored in the JSON file
	for key, value in lnCode.items():
		if key == 'NCIC CODE':
			print("NCIC CODE\n")
			print(str(value) + "\n")
		elif key == 'DISTRICT':
			print("DISTRICT\n")
			print(str(value) + "\n")
		elif key == 'BEAT':
			print("BEAT\n")
			print(str(value) + "\n")
   
def displayBeatNum():
	#Open up file
	filename = "/Users/trando/Desktop/coding/python/Python/Week 6/PROJECT1/crime.csv"
	with open(filename) as file:
		data_from_file = csv.reader(file)
		#Asks user for beat number
		print("What beat number would you like to see the crime of?\n")
		beatNum = raw_input()
		for row in data_from_file:
			#Searches 3rd row since thats where beat number is
			temp = row[3]
			#If statement for blank beat numbers
			if len(beatNum) == 0 or ' ' in beatNum:
				if(temp[0] == " "):
					print(row[5])
			#Beat numbers that are not spaces
			else:
				if(temp[0:2] == beatNum):
					print(row[5])
	 
def displayBar():
	#Path to csv file
	filename = "/Users/trando/Desktop/coding/python/Python/Week 6/PROJECT1/crime.csv"
	#localised variables
	ncicList = []
	countList = [0,0,0,0,0]
	#Asks user to enter the NCIC number
	print("Enter in 5 NCIC Numbers:\nEnter:")
	for a in range (0,5):
		temp = input()
		#Appends number to list
		ncicList.append(temp)
	
	#Finds the count for specified numbers
	countList = findCount(filename, countList, 6, ncicList)
	
	#Asks to enter chart title
	title = raw_input("Enter title of chart:\n")
 
	#Labels chart
	plt.title(str(title))
	plt.xlabel("ncicList")
	plt.ylabel("countList")
	
	#Graphs ans saved chart
	plt.tick_params(axis='both')
	plt.bar(ncicList, countList, color = "maroon", width = 200)
	plt.savefig('/Users/trando/Desktop/coding/python/Python/Week 6/PROJECT1/myplot.png')
	plt.show()
 
flag = 0

while (flag !=4 ):
	print("Which option would you like to choose?")
	print("1. Display crime report")
	print("2. Display crime by beat number")
	print("3. Create bar chart for NCIC number")
	print("4. Exit")
	flag = int(input("Enter Choice:\n"))
	if(flag == 1):
		displayCrimeReport()
	elif(flag == 2):
		displayBeatNum()
	elif(flag == 3):
		displayBar()
	elif(flag != 4):
		print("Not a valid choice.")
		

			