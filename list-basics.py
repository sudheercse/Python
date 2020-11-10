mystocks = []
mystocks = ['AAPL', 'F', 'MSFT']
print mystocks
mystocks.append('QCOM')
print mystocks
mystocks.insert(0,'GOOG')
print mystocks
mystocks.pop()
print mystocks
x=sorted(mystocks)
print x
if 'GM' in x:
    print "GM is in stocks"
else:
    print "GM is not in stocks"

