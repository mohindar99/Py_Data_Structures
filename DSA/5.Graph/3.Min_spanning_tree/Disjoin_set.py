class disjoint_set:
    def __init__(self,vertices):
        self.vertices=vertices
        self.parent={}
        for v in vertices:
            self.parent[v]=v
        self.rank=dict.fromkeys(vertices,0)

    def find(self,item):
        if self.parent[item]==item:
            return item
        else:
            return self.find(self.parent[item])

    def union(self,x,y):
        xroot=self.find(x)
        yroot=self.find(y)
        if self.rank[xroot]<self.rank[yroot]:
            self.parent[xroot]=yroot
        elif self.rank[xroot]>self.rank[yroot]:
            self.parent[yroot]=xroot
        else:
            self.parent[yroot]=xroot
            self.rank[xroot]+=1


vertices=["A","B","C","D","E"]
cust_dis=disjoint_set(vertices)
cust_dis.union("A","B")
cust_dis.union("A","D")

