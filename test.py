MyName = "Flintstone"
MyNum = 0

MyNum = input("How maby letters doi you want to see?")
MyNum = int(MyNum)

while(MyNum < len(MyName)):
    print(MyNum)
    MyNum = MyNum + 1
    
MyNum = "0"

print(type(MyNum))