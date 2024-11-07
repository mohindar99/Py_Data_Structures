class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children

    def __str__(self,level=0):
        ret=" " * level + str(self.data) + "\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

    def addchild(self,Treenode):
        self.children.append(Treenode)


Drinks=TreeNode('Drinkes',[])
cold=TreeNode('Cold',[])
hot=TreeNode("Hot",[])
tea=TreeNode('Tea',[])
coffee=TreeNode('Coffee',[])
alcohol=TreeNode('Alcohol',[])
non_alcohol=TreeNode('Non-alcohol',[])




Drinks.addchild(cold)
Drinks.addchild(hot)
hot.addchild(tea)
hot.addchild(coffee)
cold.addchild(alcohol)
cold.addchild(non_alcohol)


print(Drinks)