import math
import random

class Item():
    def __init__(self, name, itemid,minchance, maxchance,minvalue,maxvalue):
        self.name=name
        self.itemid=itemid
        self.minchance=minchance
        self.maxchance=maxchance
        self.minvalue=minvalue
        self.maxvalue=maxvalue

    def getname(self):
        return self.name
    
    def getvalue(self):
        return random.randint(self.minvalue,self.maxvalue)

    def getlowroll(self):
        return self.minvalue

    def itempick(self,chance):
        return self.minchance<chance<self.maxchance

def CreateBarterList():

    ItemList=[]

    ItemList.append(Item("Enchanted Book with Soul Speed",0,0,109,1,1))
    ItemList.append(Item("Iron Boots", 1,109,283,1,1))
    ItemList.append(Item("Splash Potion of Fire Resistance",2, 283, 457, 1, 1))
    ItemList.append(Item("Potion of Fire Resistance",3,457,631,1,1))
    ItemList.append(Item("Water Bottle",4,631,849,1,1))
    ItemList.append(Item("Iron Nugget",5,849,1067,10,36))
    ItemList.append(Item("Ender Pearl",6,1067,1285,2,4))
    ItemList.append(Item("String",7,1285,1721,3,9))
    ItemList.append(Item("Nether Quartz",8,721,2157,5,12))
    ItemList.append(Item("Obsidian",9,2157,3028,1,1))
    ItemList.append(Item("Crying Obsidian",10,3028,3899,1,3))
    ItemList.append(Item("Fire Charge",11,3899,4770,1,1))
    ItemList.append(Item("Leather",12,4770,5641,2,4))
    ItemList.append(Item("Soul Sand",13,5641,6512,2,8))
    ItemList.append(Item("Nether Brick",14,6512,7383,2,8))
    ItemList.append(Item("Spectral Arrow",15,7383,8254,6,12))
    ItemList.append(Item("Gravel",16,8254,9125,8,16))
    ItemList.append(Item("Blackstone",17,9125,9996,8,16))

    return ItemList

def printFinalList(ResponseList,gold_count):
    StringList=["Enchanted Book with Soul Speed", "Iron Boots", "Splash Potion of Fire Resistance","Potion of Fire Resistance", "Water Bottle"
                ,"Iron Nugget","Ender Pearl","String","Nether Quartz","Obsidian","Crying Obsidian","Fire Charge","Leather","Soul Sand","Nether Brick"
                ,"Spectral Arrow","Gravel","Blackstone"]
    print("")
    print("===========Summary Table============")
    for i in range(0,18):
        print(f"{StringList[i]}: {ResponseList[i]}")

    print("====================================")
    print(f"Total Gold: {gold_count}")
    print("====================================")

def printAverageList(ResponseList,gold_count,runs):
    StringList=["Enchanted Book with Soul Speed", "Iron Boots", "Splash Potion of Fire Resistance","Potion of Fire Resistance", "Water Bottle"
                ,"Iron Nugget","Ender Pearl","String","Nether Quartz","Obsidian","Crying Obsidian","Fire Charge","Leather","Soul Sand","Nether Brick"
                ,"Spectral Arrow","Gravel","Blackstone"]

    print(f"=========== Average Summary Table of {runs} iterations ============")
    for i in range(0,18):
        print(f"{StringList[i]}: {ResponseList[i]}")

    print("====================================")
    print(f"Average Gold: {gold_count}")
    print("====================================")

class BarterList():
    def __init__(self,inputlist,counter,passed):
        self.ItemList=inputlist
        self.goldcount=counter
        self.passed=passed

        for _ in inputlist:
            counter+=1

        self.length=counter

    def additem(self,item):
        self.ItemList.append(item)

    def getitem(self):
        return self.ItemList
    
    def getlen(self):
        return self.length

    def printlist(self):
        return printFinalList(self.ItemList,self.goldcount)

    def getpassed(self):
        return self.passed

def BarterSetup():

    ItemList=CreateBarterList()
    ResponseList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    BarterHistory=[]
    BarterHistory=[]
    for i in range(5):
        ResponseList=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        counter=0
        while ResponseList[10]<1728 and counter<10750:
            number=random.randint(0,9996)
            for item in ItemList:
                if item.itempick(number):
                    ResponseList[item.itemid]+=item.getvalue()
                    print(f"Instance: {i} Item Number: {counter} Item Added:{item.name} Quantity: {item.getvalue()}")
            counter+=1
        passed=ResponseList[10]>=1728

        BarterHistory.append(BarterList(ResponseList,counter,passed))

    print("====================================")
    print("")
    print("")
    print("")
    print("")

    averagelist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    runcount=0
    averagecount=0
    success=0
    total=0
    for item in BarterHistory:
        if item.getitem()[10]>=1728:
           success+=1 
           averagecount+=item.goldcount
        total+=1

    for i in range(len(averagelist)):
            runcount=0
            for item in BarterHistory:
                if item.getpassed():
                    averagelist[i]+=item.getitem()[i]
                    runcount+=1
            averagelist[i]/=runcount
            averagelist[i]=round(averagelist[i],2)

    averagecount/=success
    printAverageList(averagelist,averagecount,runcount)

    print(f"Success Rate: {success} / {total} for a rate of {success/total*100}%")




class EyeCoords():
    def __init__(self,x,z,angle):
        self.x=x
        self.z=z
        self.angle=math.radians(angle)
        # self.angle=angle

    def getx(self):
        return self.x

    def getz(self):
        return self.z

    def getangle(self):
        return self.angle

    def printcoords(self):
        print(f"X: {self.x} Z: {self.z} Angle: {self.angle}")

    def getcoords(self):
        return [self.x,self.z,self.angle]

    def getgradient(self):
        return -(1/math.tan(self.angle))

def getLength(First,Second):
    return math.sqrt((First.getx()-Second.getx())**2+(First.getz()-Second.getz())**2)

def getAngle(First,Second):
    return math.atan((First.getz()-Second.getz())/(First.getx()-Second.getx()))#returns angle that the two points make with the Z axis

def smaLLest(First,Second):
    if First.getangle()<Second.getangle():
        return First
    else:
        return Second

def largESt(First,Second):
    if First.getangle()>Second.getangle():
        return First
    else:
        return Second

def response(largest):
    #Based on the largest angle, the quadrant can be determined
    #Quadrants work as follows:
    #SouthEast is + +
    #SouthWest is - +
    #NorthEast is + -
    #NorthWest is - -
    angle=largest.getangle()
    if 0<angle<math.pi/2:#SouthWest
        print("X: -1 Z: 1")
        return [-1,1]
    elif math.pi/2<angle<math.pi:#NorthWest
        print("X: 1 Z: -1")
        return [-1,-1]#done
    elif -math.pi/2<angle<0:#SouthEast
        print("X: 1 Z: 1")
        return [1,1]
    elif -math.pi<angle<-math.pi/2:#NorthEast
        print("X: -1 Z: -1")
        return [1,-1]
    else:
        print("Error")
        return [0,0]

def calculateCoordinates(First,Second):

    First.printcoords()
    Second.printcoords()
    smallest=smaLLest(First,Second)#Store the smallest angle
    largest=largESt(First,Second)#Store the largest angle
    [shiftx,shiftz] = response(largest)

    print("====================================")

    calc = getLength(First,Second)#Calculate the length of the line between the two points
    calc = calc/math.sin(abs(First.getangle()-Second.getangle()))#Calculate the fraction part of the sine rule

    # print(math.degrees(smallest.getangle()),math.degrees(getAngle(First,Second)),math.degrees(smallest.getangle()-abs(getAngle(First,Second))))
    # print(f"Length: {getLength(First,Second)}")
    # print(f"Angle: {math.degrees(math.sin(abs(First.getangle()-Second.getangle())))}")
    # print(f"Secondary Angle: {math.degrees(largest.getangle()-abs(getAngle(First,Second)+math.pi/2))}")


    print((getLength(First,Second)/math.sin(abs(First.getangle()-Second.getangle()))*math.sin(largest.getangle()-(getAngle(First,Second))+math.pi/2))*math.sin(smallest.getangle()))
    calc = getLength(First,Second)/math.sin(abs(First.getangle()-Second.getangle()))*math.sin(largest.getangle()-getAngle(First,Second)+math.pi/2)
    # calc = getLength(First,Second)/math.sin(abs(First.getangle()-Second.getangle()))*math.sin(smallest.getangle()-getAngle(First,Second))
    print(f"Calculated X: {smallest.getx()}, {calc*math.sin(smallest.getangle())}")
    print(f"Calculated Z: {smallest.getz()}, {calc*math.cos(smallest.getangle())}")
    x= shiftx*smallest.getx() + calc*math.sin(smallest.getangle())
    z= calc*math.cos(smallest.getangle()) + shiftz*smallest.getz()

    # print(f"Proper Coordinates: {x} {z}")
    # print(f"Nether Coordinates: {x/8} {z/8}")
    return x,z

def WithinRange(inputnum, factor, actual):
    if inputnum<actual*(1+factor) and inputnum>actual*(1-factor):
        return True
    print(f"Input: {inputnum} Actual: {actual}")
    return False

def Test(x,z,actualx,actualz, testinput):
    if WithinRange(abs(x),0.5,abs(actualx)) and WithinRange(abs(z),0.5,abs(actualz)):
        print("Test Passed")
        return testinput+1
    else:
        print("Test Failed")
        return testinput

def StrongHoldCalculator():
    # FirstSetInput = input("What is the X and Z coordinate of the first throw?\n")
    # [FirstSetX, FirstSetZ] = FirstSetInput.split(" ")
    # FirstAngle = input("What is the angle of the first throw?\n")
    # SecondSetInput = input("What is the X and Z coordinate of the second throw?\n")
    # [SecondSetX, SecondSetZ] = SecondSetInput.split(" ")
    # SecondAngle = input("What is the angle of the second throw?\n")

    # FirstSetX = float(FirstSetX)
    # FirstSetZ = float(FirstSetZ)
    # FirstAngle = float(FirstAngle)
    # SecondSetX = float(SecondSetX)
    # SecondSetZ = float(SecondSetZ)
    # SecondAngle = float(SecondAngle)

    # calculateCoordinates(EyeCoords(FirstSetX,FirstSetZ,FirstAngle),EyeCoords(SecondSetX,SecondSetZ,SecondAngle))

    #Test 1
    testcounter=0
    print("====Test 1====")
    First=EyeCoords(-156.7,-178.7,100.2)
    Second=EyeCoords(-129.7,-199.7,99)
    [x,z]=calculateCoordinates(First,Second)
    print("Actual Coords: -1352, -398")
    testcounter=Test((x),(z),(-1352),(-398),testcounter)

    # #Test 2
    print("====Test 2====")
    First = EyeCoords(-1374.7, 234.3, -177.9)
    Second = EyeCoords(-1345.7, 205.3, 179.4)
    [x,z]=calculateCoordinates(First,Second)
    print("Actual Coords: -1352, -398")
    testcounter=Test((x),(z),(-1352),(-398), testcounter)
    print("=== Summary ===")
    print(f"Test Passed: {testcounter} / 2")

def main():
    
    StrongHoldCalculator()
    # print("Options List:")
    # print("Overworld")
    # print("1. Stronghold Calculation")
    # print("Nether")
    # print("1. Bartering")
    # response = int(input("Please select an option: "))
    # if response==1:
    #     StrongHoldCalculator()
    # elif response==2:
        # BarterSetup()


main()