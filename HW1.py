#   Create a program that asks a suser for
#   their name and two numbers and then prints
#   out the user name and the sum of those two
#   numbers in a single sentence, such as
#   "Hello Fred, the sum of your two numbers is 13."

#   Asks user to input name and two numbers
#   Inputted name is defined as a string value
#   Inputted numbers are defined as integer values

name = input("Enter a name:\n")
n1 = int(input("Enter an integer number:\n"))
n2 = int(input("Enter another integer number:\n"))

#   Prints out name and sum of the two integers entere

print("Hello " + name + ", the sum of your two numbers is " + str(n1 + n2) + ".")
