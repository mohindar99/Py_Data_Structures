

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

# This is the method used to traverse the graph
    def BFS(self,vertex):
        visited=set()
        visited.add(vertex)
        queue=[vertex]
        while queue:
            curr=queue.pop(0)
            print(curr)
            for adj in self.gdict[curr]:
                if adj not in visited :
                    visited.add(adj)
                    queue.append(adj)


    def DFS(self,vertex):
        visited=set()
        stack=[vertex]
        while stack:
            curr=stack.pop()
            if curr not in visited:
                print(curr)
                visited.add(curr)

            for adj in self.gdict[curr]:
                if adj not in visited:
                    stack.append(adj)






custDict={"a":["b",'c'],
          'b':['a','d','e'],
          'c':['a','e'],
          'd':['b','e','f'],
          'e':['d','f'],
          'f':['d','e']
          }

graph=Graph(custDict)
graph.DFS('a')