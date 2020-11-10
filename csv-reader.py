import csv

def getStockDict():
    dataFile = "companylist.csv"
    f = open(dataFile, "r")
    reader = csv.reader(f)
    myDict={}
    for data in reader:
        myDict[data[0]]= data[1]
    return myDict

myDict = getStockDict()
myStocks = ['A', 'X', 'L', 'AA']
for x in myStocks:
    if x in myDict:
        print myDict[x]
    else:
        print "not found"
