import json

numbers = [2, 3, 5, 7, 11,22,33,44,55,66, 99]

filename = 'C:/Users/draus/Desktop/Spring_2020b/Week6/Chapter_10/numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)
