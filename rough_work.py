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
# #         if self.root==None:
# #             self.root=BSTNode(value)
# #
# class BSTNode:
#     def __init__(self,data):
#         self.data=data
#         self.leftchild=None
#         self.rightchild=None
#
# custBST=BSTNode(None)
#
# if custBST.data is None:
#     print("The node is empty")

# node={'l':23,'S':45,'r':56}
# print(len(node))

# car={'brand':'ford','Model':'Mustang','Year':2023}
# x=car.values()
# car['Year']=2010
# print(x)

# sam={'a':2323,'b':456,'c':9874}
# val=sam.pop('a')
# print(val)
# print(sam)

def fibutill(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fibutill(n-1)+fibutill(n-2)

def fib(n):
    for i in range(1,n+1):
        print(fibutill(i))

fib(4)