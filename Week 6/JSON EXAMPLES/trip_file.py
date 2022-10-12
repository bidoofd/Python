import json

#create a blank dictionary
people = {}
filename = 'C:/Users/Tran/Desktop/coding/python/Week 6/JSON EXAMPLES/places.json'


#look for old data and if found read in the old data intohte empty dictionary - people
try:
	with open(filename) as json_file:  
		people = json.load(json_file)
except FileNotFoundError:
# if no old dtaa found, inform th euser, but no other action made
	print ("No old data to load.\n")
	input("Press Enter to continue...")
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and age.
    name = input("\nWhat is your name? ")
    age = input("How old are you? ")
    people[name] = age
#note the 'w' in the open command.  This means we are overwritnghte entire file
#Since we read in the old data and add otthe dictionary in memory the overwrite
#still contains all of the old data
    with open(filename, 'w') as file_object:
        json.dump(people, file_object)
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



#we COULD just print from the dictionary since it still holds the data but here is the code
#to read the dictionary from the file - 
#with open(filename) as json_file:  
#	people = json.load(json_file)



#remember that the .items method for a dictionary returns both the index number and the
#stored value associated with it
for name,ages in people.items():
	print(name + " is "+ ages + " years old.")
        
#just a pause before ending the program
input("Press Enter to continue...")
