# class BSTNode:
#     def __init__(self,data):
#         self.data=data
#         self.leftchild=None
#         self.rightchild=None
#
# class BST:
#     def __init__(self):
#         self.root=None
#
#     def checkNode(self,rootNode):
#         print(rootNode)
#         if rootNode is None:
#             return rootNode
#
#     def insert(self,value):
#         if self.root==None:
#             self.root=BSTNode(value)
#
class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

custBST=BSTNode(None)

if custBST.data is None:
    print("The node is empty")