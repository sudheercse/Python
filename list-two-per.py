import csv

count=0
twoPercent = []
stocks = ['aapl', 'f']
for stk in stocks:
    myfile=open("IEX_stock-" + stk +"-chart-1y.csv", "r")
    reader = csv.reader(myfile)
    headers = next(reader, None) # column headers
    #print(headers)
    for x in reader:
        #date, open, close, volume
        cls = float(x[4])
        opn = float(x[1])
        chg = (cls-opn)/opn
        if chg >0.02:
            #print stk + " " + str(chg)
            twoPercent.append(x[0] + " " + stk + " " + str(chg))
            count = count+1
print count
for x in sorted(twoPercent):
    print x
