INF=9999

def printSol(nV,distance):
    for i in range(nV):
        for j in range(nV):
            if distance==INF:
                print("INF",end=" ")
            else:
                print(distance[i][j],end=" ")
        print("")

def Floyd_warshall_algo(nV,G):
    distance=G
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

    printSol(nV,distance)


G=[[0,8,INF,1],
   [INF,0,1,INF],
   [4,INF,0,INF],
   [INF,2,9,0]]

Floyd_warshall_algo(4,G)

