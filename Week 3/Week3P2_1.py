# Make an empty list
# Make a second list that contains three names
# Add two items to the first list
# Add the list to the first list
# Add two more items to the first list
# Print out the first list

list1 = []
list2 = ["Tiffany", "Sarah", "Austin"]

list1.append("Jacob")
list1.append("Josh")
for a in range(len(list2)):
    list1.append(list2[a])
list1.append("Gyro")
list1.append("Dylan")

for a in range(len(list1)):
    print("Item #: " + str(a+1) + " " + list1[a])