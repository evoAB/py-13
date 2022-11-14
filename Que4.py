thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
k=0
for i in thislist:
    if(i=="SQL"):
        thislist[thislist.index(i)]="NoSQL"
    if(i=="Reactnative"):
        thislist[thislist.index(i)]="Flutter"
print(thislist)