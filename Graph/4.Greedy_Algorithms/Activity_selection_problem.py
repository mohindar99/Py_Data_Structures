activities=[["A1",0,6],
            ["A2",3,4],
            ["A3",1,2],
            ["A4",5,8],
            ["A5",5,7],
            ["A6",8,9]]

def getMaxActivities(act):
    act.sort(key=lambda i:i[2])
    i=0
    firstA=act[i][0]
    print(firstA)
    for j in range(len(act)):
        if act[i][2]<act[j][1]:
            print(act[j][0])
            i=j

getMaxActivities(activities)

