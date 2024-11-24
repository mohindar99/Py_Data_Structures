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
import heapq
from platform import mac_ver


# Output: 4


def even(arr):
    arr1=[i for i in arr if i%2==0]
    if not arr1 :
        return 0
    else:
        return max(arr1)

def getMinOperations(CT):
    count=0
    while True:
        max_val=even(CT)
        if max_val==0:
            break
        for i in range(len(CT)):
            if CT[i]==max_val:
                CT[i]=CT[i]/2
        count+=1
    return count

# Example usage:
n = 4
computationalTime = [2,4,8,16]
print(getMinOperations(computationalTime))  # Output: 4
