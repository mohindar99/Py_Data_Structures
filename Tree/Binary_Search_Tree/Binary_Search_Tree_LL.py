from ast import NodeVisitor
from re import search

import Queues.queue_linkedlist as queue



class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data=nodeValue
    elif nodeValue<=rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftchild,nodeValue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild=BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightchild,nodeValue)
    return "The node had been inserted successfully"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inorderTraversal(rootNode):
    if not rootNode:
        return
    inorderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inorderTraversal(rootNode.rightchild)


def postorderTraversal(rootNode):
    if not rootNode:
        return
    postorderTraversal(rootNode.leftchild)
    postorderTraversal(rootNode.rightchild)
    print(rootNode.data)

def levelorderTraversal(rootNode):
    if not rootNode:
        return
    customequeue=queue.Queue()
    customequeue.enqueue(rootNode)
    while not (customequeue.isEmpty()):
        root=customequeue.dequeue()
        print(root.value.data)
        if root.value.leftchild is not None:
            customequeue.enqueue(root.value.leftchild)
        if root.value.rightchild is not None:
            customequeue.enqueue(root.value.rightchild)

def searchNode(rootNode,nodeValue):
    if rootNode.data==nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        searchNode(rootNode.leftchild,nodeValue)
    else:
        searchNode(rootNode.rightchild,nodeValue)


def minNodeValue(rootNode):
    current=rootNode
    while current.left is not None:
        current=current.leftchild
    return current

def deletenodeValue(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftchild=deletenodeValue(rootNode.leftchild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightchild = deletenodeValue(rootNode.rightchild,nodeValue)
    else:
        if rootNode.leftchild is None:
            temp=rootNode.rightchild
            rootNode=None
            return temp

        if rootNode.rigthchild is None:
            temp=rootNode.leftchild
            rootNode=None
            return temp

        temp=minNodeValue(rootNode.rightchild)
        rootNode.data=temp.data
        rootNode.rightchild=deletenodeValue(rootNode.rightchild,temp.data)
    return rootNode


def deleteentireBST(rootNode):
    rootNode.data=None
    rootNode.leftchild=None
    rootNode.rightchild=None
    return "The node had been deleted successfully"

custBST=BSTNode(None)
insertNode(custBST,45)
insertNode(custBST,56)
insertNode(custBST,89)
insertNode(custBST,100)
levelorderTraversal(custBST)
print("The break")
deleteentireBST(custBST)
levelorderTraversal(custBST)


