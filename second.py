l = [4,9999,2,4,4,8,4]

myDict = dict()
for i in l:
    if i not in myDict:
        myDict[i] = 1
    else:
        myDict[i] += 1

for i,j in myDict.items():
    if j>=len(l)//2:
        print(i)
        break
