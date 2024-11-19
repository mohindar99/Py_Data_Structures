import heapq

class Edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex


class Node:
    def __init__(self,name):
        self.name=name
        self.visited=False
        self.predessor=None
        self.neightbour=[]
        self.min_distance=float('inf')

    def addEdge(self,weight,target_vertex):
        edge=Edge(weight,self,target_vertex)
        self.neightbour.append(edge)

    def __lt__(self, other):
        return self.min_distance<other.min_distance


class Dijkstra_Algo:
    def __init__(self):
        self.heap=[]

    def calculate(self,start_vertex):
        start_vertex.min_distance=0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            actual_vertex=heapq.heappop(self.heap)
            # checking weather it is already visited or not
            if actual_vertex.visited:
                continue

            for edge in actual_vertex.neightbour:
                start=edge.start_vertex
                target=edge.target_vertex
                new_distance=start_vertex.min_distance+edge.weight

                if new_distance<target.min_distance:
                    target.min_distance=new_distance
                    target.predessor=start

                    #update heap
                    heapq.heappush(self.heap,target)
            actual_vertex.visited=True

    def shortest_Path(self,vertex):
        print(f"The shortest path to the vertex is {vertex.min_distance}")
        actual_vertex=vertex
        while actual_vertex is not None:
            print(actual_vertex.name," ")
            actual_vertex=actual_vertex.predessor

nodeA=Node("A")
nodeB=Node("B")
nodeC=Node("C")
nodeD=Node("D")
nodeE=Node("E")
nodeF=Node("F")
nodeG=Node("G")
nodeH=Node("H")


nodeA.addEdge(6,nodeB)
nodeA.addEdge(10,nodeC)
nodeA.addEdge(9,nodeD)

nodeB.addEdge(5,nodeD)
nodeB.addEdge(16,nodeE)
nodeB.addEdge(13,nodeF)

nodeC.addEdge(6,nodeD)
nodeC.addEdge(5,nodeH)
nodeC.addEdge(21,nodeG)

nodeD.addEdge(8,nodeF)
nodeD.addEdge(7,nodeH)

nodeE.addEdge(10,nodeG)

nodeF.addEdge(4,nodeE)
nodeF.addEdge(12,nodeG)

nodeH.addEdge(2,nodeF)
nodeH.addEdge(14,nodeG)

algorithm=Dijkstra_Algo()
algorithm.calculate(nodeA)

algorithm.shortest_Path(nodeB)










