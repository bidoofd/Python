# Prints out a list with a number while the information is user entered

# Initialised variables
item = ""
size = 0

# Asks user to enter in size of list and initialises size
size = int(input("How many items do you want to enter?\n"))
list = range(size)

# Asks user to enter in an item
print("Enter in the items:")
for a in range(len(list)):
    item = raw_input()
    # Replaces item in the list
    list[a] = item

# Prints out item in list with appropriate list number
print("Items in the list:")
for b in range(len(list)):
    print("Item #: " + str(b+1) + " " + list[b])