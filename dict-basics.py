myDict = {}
print myDict
myDict['ABC']="Company ABC"
myDict['XYZ']="Corporation XYZ"
myDict['ZZZ']="Company ZZZ"
print myDict
del myDict['ZZZ']
print myDict
myDict['XYZ']="Updated company XYZ"
print myDict
if 'XYZ' in myDict:
    print "True"
print "ABC" not in myDict.keys()
print "Company V" in myDict.values()
for x in myDict.keys():
    print x

for x in myDict.values():
    print x

for x in myDict:
    print x, myDict[x]
