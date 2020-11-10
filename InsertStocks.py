import csv
import sqlite3

stockDict = {}
myList = []
with open('myData.csv', 'w') as f:
    stocks = ['aapl', 'f']
    for stk in stocks:
        myfile=open("IEX_stock-" + stk +"-chart-1y.csv", "r")
        reader = csv.reader(myfile)
        headers = next(reader, None) # column headers
        #print(headers)
        count=0
        for x in reader:
            #date, close, volume
            myTuple = (x[0], x[1], x[2], x[3], x[4], x[5], stk)
            myList.append(myTuple)
    print len(myList)
    
    myfile.close()
f.close()
print("done")

conn=sqlite3.connect("C://Python27/mycode/db/stocks.db")
c = conn.cursor()

c.executemany('Insert into stockprices values(?,?,?,?,?,?,?)', myList)
conn.commit()
conn.close()
print c.rowcount
