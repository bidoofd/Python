# For homework, create a program that asks a user for their name and two numbers
# and then prints out the user's name and the sum of those two numbers in a single
# sentence, such as "Hello Fred, the sum of your two numbers is 13."

name = raw_input("Enter your namne:")
x = int(input("Enter in a number: "))
y = int(input("Enter another number: "))

print("Hello " + name + ", the sum of your two numbers is " + str(x+y) + ".")