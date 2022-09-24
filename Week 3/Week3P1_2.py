#For loop that goes through a number list, prints out sum and average

list = [1,2,3,4,5,6,7,8,9,10]
sum = 0

for a in range(len(list)):
    sum = sum + list[a]

print("The sum of the list is: " + str(sum) + "\n")
print("The average of the list is: " + str(sum/len(list)) + "\n")
