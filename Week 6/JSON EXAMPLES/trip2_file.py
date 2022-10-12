import json
places = {}
#Lets make this more interesting...and more complicted
#we will not jsut store the name and the age, but a list of informaiton associated with
#the key value - name
#so the dictionary will store name:list
places['people'] = []  

#notice I used relative addressing in this file
filename = 'places2.json'


try:
	with open(filename) as json_file:  
		places = json.load(json_file)
except FileNotFoundError:
	print ("No old data to load.\n")
    
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
	name = input("\nWhat is your name? ")
	country = input("What country would you like to visit? ")
	city = input("What city would you like to visit in "+ country + " ")
	money = input("how much do you think you would spend? ")
	importance = input("An a scale of 1-5 how important is this trip to you?")
	if importance == '1':
		importance = 'Barely Interested'
	elif importance == '2':
		importance = 'mildly Interested'
	elif importance == '3':
		importance = 'Excited'
	elif importance == '4':
		importance = 'Very Excited'
	elif importance == '5':
		importance = 'Extreamley Excited'
	else:
		importance = 'Not Determined.'

#append the informaiton to the dictionary
	places['people'].append({  
		'Name': name,
		'Country': country,
		'City': city,
		'Money': money,
		'Importance': importance
	})

    
#write the dictionary tothe file
	with open(filename, 'w') as file_object:
		json.dump(places, file_object)
		
		
		
    # Find out if anyone else is going to take the poll.
	ques = True
	while ques:
		repeat = input("\nWould you like to\n 1. let another person respond. \n 2. See the results and Quit ")
		if repeat == '1' or repeat == '1.':
			ques = False
		elif repeat == '2' or repeat == '2.':
			ques = False
			polling_active = False


# Polling is complete. Show the results.
print("\n--- Poll Results ---")



#we don't actually need to read the file, but since we are learing I have incuded it here
with open(filename) as json_file:  
    places = json.load(json_file)
    
#Notice how to access the elements in the list that is inside of the dictionary
    for p in places['people']:
        print('Name: ' + p['Name'])
        print('Country: ' + p['Country'])
        print('City:  ' + p['City'])
        print('Money:  ' + p['Money'])
        print('Importance:  ' + p['Importance'])               
        print('')

input("Press Enter to continue...")
