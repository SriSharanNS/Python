list=[2,5,6,2,4,6,4,7,8]
print(list)
newlist=[]
for item in list:
    if item not in newlist:
        newlist.append(item)
print(newlist)  

names=["narchos","brazil","new york","narchos","brazil","los vegas"]
print(names)
newnames=[]
for item in names:
    if item not in newnames:
        newnames.append(item)
print(newnames)        