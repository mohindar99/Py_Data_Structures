class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def addVertex(self,vertex):
        if vertex in self.gdict.keys():
            return False
        self.gdict[vertex]=[]
        return True
    def print_graph(self):
        for vertex in self.gdict:
            print(vertex,":",self.gdict[vertex])

    def addEdges(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
             self.gdict[vertex1].append(vertex2)
             self.gdict[vertex2].append(vertex1)
             return True
        return False

    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
            return True
        return False

    def remove_vertex(self,vertex):
        if vertex in self.gdict.keys():
            for other_vertex in self.gdict[vertex]:
                self.gdict[other_vertex].remove(vertex)
            del self.gdict[vertex]
            return True
        return False


    def bfs_ssp(self,start,end):
        queue=[[start]]
        while queue:
            path=queue.pop(0)
            node=path[-1]
            if node==end:
                return path
            else:
                for i in self.gdict[node]:
                    new_path=list(path)
                    new_path.append(i)
                    queue.append(new_path)



custDict={"a":["b",'c'],
          'b':['d','g'],
          'c':['d','e'],
          'd':['f'],
          'e':['f'],
          'g':['f']
          }

graph=Graph(custDict)
print(graph.bfs_ssp("a","e"))