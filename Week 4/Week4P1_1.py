# Using the menu program(from last week) as a starting point.  Make up some functions in the same file to:
# 1. Allow the user to enter their name
# 2.Print out the users name
# 3.Say 'Hello" to the user
# 4.Tell the user the number of characters in their name

loop = 1
names = []

def enterName():
    name = raw_input("Enter your name: ")
    return name

def printName(names):
    print(names)

def sayHello():
    print("Hello")


while (loop ==1):
    print("\tMENU")
    print("1. Enter name")
    print("2. Print name")
    print("3. Say Hello")
    print("4. Clear List")
    print("5. # of character's in name")
    print("6. Exit")
    user_input = raw_input("==>")
    if (user_input == "1"):
        temp = enterName()
        if (len(temp) >0):
            names.append(temp)
            print("name added")
        else:
            print("name not added")
    elif (user_input == "2"):
        printName(names)
    elif (user_input == "3"):
        sayHello()
    elif (user_input == "4"):
        sure = raw_input("Are you sure? (y/n)")
        if (sure == "Y" or sure == "y"):
            names.clear()
            print("List cleared!!")
        else:
            print("not cleared")
    elif(user_input == "5"):
        for a in range(len(names)):
            print("Name in position " + str(a) + " in list: " + names[a])
        choice = int(input("Which name do you want to know how many characters there are in it?"))
        length = len(names[choice])
        print(names[choice] + " has " + str(length) + " characters.")
    elif (user_input == "6"):
        loop = 0
    else:
        print ("error message")
    