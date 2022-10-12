import json

filename = 'C:/Users/draus/Desktop/Spring_2020b/Week6/Chapter_10/username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")
