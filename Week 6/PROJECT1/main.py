import csv
import json

def findCount(fn, countList, rowNum):
    with open(fn) as file:
        data_from_file = csv.reader(file)
        header_row = next(data_from_file)
        for index,column_header in enumerate(header_row):
            print(index,column_header)
    
        #Creates a list for the count on codes in the range
        #Finds and stores data in row 6 where the NCIC code is
        for row in data_from_file:
            temp = row[rowNum]
            if(temp.isdigit() == True):
                temp = int(temp)
                if(temp % 10 < 10):
                    if(temp == 1):
                        countList[0] = countList[0] +1
                    elif (temp == 2):
                        countList[1] = countList[1] +1		
                    elif (temp == 3):
                        countList[2] = countList[2] +1
                    elif (temp == 4):
                        countList[3] = countList[3] +1
                    elif (temp == 5):
                        countList[4] = countList[4] +1
                    elif (temp == 6):
                        countList[5] = countList[5] +1
                else:
                    if temp >= 0 and temp <= 999:
                        countList[0] = countList[0] +1
                    elif temp >= 1000 and temp <= 1999:
                        countList[1] = countList[1] +1		
                    elif temp >= 2000 and temp <= 2999:
                        countList[2] = countList[2] +1
                    elif temp >= 3000 and temp <= 3999:
                        countList[3] = countList[3] +1
                    elif temp >= 4000 and temp <= 4999:
                        countList[4] = countList[4] +1
                    elif temp >= 5000 and temp <= 5999:
                        countList[5] = countList[5] +1
                    elif temp >= 6000 and temp <= 6999:
                        countList[6] = countList[6] +1
                    elif temp >= 7000 and temp <= 7999:
                        countList[7] = countList[7] +1
                    elif temp >= 8000 and temp <= 8999:
                        countList[8] = countList[8] +1
                    elif temp >= 9000 and temp <= 9999:
                        countList[9] = countList[9] +1
            else:
                if(chr(ord(temp[0:1])) == "1"):
                    if(temp[1:2]  == "A"):
                        countList[1] = countList[1] + 1
                    elif(temp[1:2]  == "B"):
                        countList[2] = countList[2] + 1
                    elif(temp[1:2]  == "C"):
                        countList[3] = countList[3] + 1
                    elif(temp[1:2]  == "M"):
                        countList[4] = countList[4] + 1
                elif(chr(ord(temp[0:1])) == 2):
                    if(temp[1:2]  == "A"):
                        countList[5] = countList[5] + 1
                    elif(temp[1:2]  == "B"):
                        countList[6] = countList[6] + 1
                    elif(temp[1:2]  == "C"):
                        countList[7] = countList[7] + 1
                    elif(temp[1:2]  == "M"):
                        countList[8] = countList[8] + 1
                elif(chr(ord(temp[0:1])) == 3):
                    if(temp[1:2]  == "A"):
                        countList[9] = countList[9] + 1
                    elif(temp[1:2]  == "B"):
                        countList[10] = countList[10] + 1
                    elif(temp[1:2]  == "C"):
                        countList[11] = countList[11] + 1
                    elif(temp[1:2]  == "M"):
                        countList[12] = countList[12] + 1
                elif(chr(ord(temp[0:1])) == 4):
                    if(temp[1:2]  == "A"):
                        countList[13] = countList[13] + 1
                    elif(temp[1:2]  == "B"):
                        countList[14] = countList[14] + 1
                    elif(temp[1:2]  == "C"):
                        countList[15] = countList[15] + 1
                    elif(temp[1:2]  == "M"):
                        countList[16] = countList[16] + 1
                elif(chr(ord(temp[0:1])) == 5):
                    if(temp[1:2]  == "A"):
                        countList[17] = countList[17] + 1
                    elif(temp[1:2]  == "B"):
                        countList[18] = countList[18] + 1
                    elif(temp[1:2]  == "C"):
                        countList[19] = countList[19] + 1
                    elif(temp[1:2]  == "M"):
                        countList[20] = countList[20] + 1
                elif(chr(ord(temp[0:1])) == 6):
                    if(temp[1:2]  == "A"):
                        countList[21] = countList[21] + 1
                    elif(temp[1:2]  == "B"):
                        countList[22] = countList[22] + 1
                    elif(temp[1:2]  == "C"):
                        countList[23] = countList[23] + 1
                    elif(temp[1:2]  == "M"):
                        countList[24] = countList[24] + 1
                elif(temp[0:1] == " "):
                    countList[25] = countList[25] + 1
                    
                
    return countList
                    
#Function to display crime report
def displayCrimeReport():
    #Variables declared
    lnCode = {}
    lnCode['NCIC CODE'] = []
    lnCode['DISTRICT'] = []
    lnCode['BEAT'] = []
    ncic_code_count = [0,0,0,0,0,0,0,0,0,0]
    district_count = [0,0,0,0,0,0]
    beat_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    fJSON = "C:/Users/Tran/Desktop/coding/python/Week 6/PROJECT1/January.json"
    filename = "C:/Users/Tran/Desktop/coding/python/Week 6/PROJECT1/crime.csv"
    
    ncic_code_count = findCount(filename, ncic_code_count, 6)
    district_count = findCount(filename, district_count, 2)
    beat_count = findCount(filename, beat_count, 3)

    try:
        with open(fJSON) as json_file:  
            lnCode = json.load(json_file)
    except  FileNotFoundError:
    # if no old data found, inform th euser, but no other action made
        print ("No old data to load.\n")
        input("Press Enter to continue...")
        # Set a flag to indicate that polling is active.
    polling_active = True
        
    var2 = 0
    var3 = 999
    count = 0
    while polling_active:
        for a in range(0,10):
            # Prompt for the person's name and age.
            
            text = ("NCIC Code Count from range " + str(var2) + "-" + str(var3) + ": ")
            lnCode['NCIC CODE'] = (text + str(ncic_code_count[count]))
            var2 = var2 + 1000
            var3 = var3 + 1000
            count = count + 1
        #for b in range(0,6):
        #    text = ("Disctrict Count: ")
        #    lnCode['DISTRICT'] = (text + str(district_count[count]))
        #    count = count + 1
        #for c in range(0,25):
        #    text = ("Beat Count: ")
        #    lnCode['BEAT'] = (text + str(beat_count[count]))
        #    count = count + 1
        polling_active = False
        
    lnCode.append({
        'NCIC CODE': lnCode['NCIC CODE'],
        #'DISTRICT': lnCode['DISTRICT'],
        #'BEAT': lnCode['BEAT'],
    })    
    
    polling_active = True
    
    while polling_active:
        with open(fJSON, 'w') as file_object:
            json.dump(lnCode, file_object)
        polling_active = False
    # Find out if anyone else is going to take the poll.
    
    print("COUNT ALL CRIMES BY CODE")
    print("COUNT ALL CRIMES BY DISTRICT")
    print("COUNT ALL CRIMES BY BEAT")
        
flag = 0


while (flag !=4 ):
    print("Which option would you like to choose?")
    print("1. Display crime report")
    print("2. Display crime by beat number")
    print("3. Create bar chart for NCIC number")
    print("4. Exit")
    flag = int(input("Enter Choice:\n"))
    if(flag == 1):
        displayCrimeReport()
    elif(flag == 2):
        print("")
    elif(flag == 3):
        print("")
    elif(flag != 4):
        print("Not a valid choice.")
        

            