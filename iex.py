import csv

with open('myData.csv', 'w') as f:
    stocks = ['aapl', 'f']
    for stk in stocks:
        myfile=open("IEX_stock-" + stk +"-chart-1y.csv", "r")
        reader = csv.reader(myfile)
        headers = next(reader, None) # column headers
        #print(headers)
        count=0
        for x in reader:
            #date, open, close, volume
            f.write(stk + "," + x[0] + "," + x[1] + "," + x[4] + "," + x[5]+ "\n")
            count = count+1
        print count
        myfile.close()
f.close()
print("done")
