import Queues.queue_linkedlist as queue

class AVLTree:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
        self.height=1

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


def getHeight(rootNode):
    if not rootNode :
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot=disbalanceNode.leftchild
    disbalanceNode.leftchild=disbalanceNode.leftchild.rightchild
    newRoot.rightchild=disbalanceNode
    disbalanceNode.height=1+max(getHeight(disbalanceNode.leftchild),getHeight(disbalanceNode.rightchild))
    newRoot.height=1+max(getHeight(newRoot.leftchild),getHeight(newRoot.rightchild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot=disbalanceNode.rightchild
    disbalanceNode.rightchild=disbalanceNode.rightchild.leftchild
    newRoot.leftchild=disbalanceNode
    disbalanceNode.height=1+max(getHeight(disbalanceNode.leftchild),getHeight(disbalanceNode.rightchild))
    newRoot.height=1+max(getHeight(newRoot.leftchild),getHeight(newRoot.rightchild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftchild)-getHeight(rootNode.rightchild)

def insertNode(rootNode,nodeValue):
    if not rootNode:
        return AVLTree(nodeValue)
    elif nodeValue<rootNode.data:
        rootNode.leftchild=insertNode(rootNode.leftchild,nodeValue)
    else:
        rootNode.rightchild=insertNode(rootNode.rightchild,nodeValue)
    rootNode.height=1+max(getHeight(rootNode.leftchild),getHeight(rootNode.rightchild))
    balance=getBalance(rootNode)
    if balance>1 and nodeValue<rootNode.leftchild.data:
        return rightRotate(rootNode)
    if balance>1 and nodeValue>rootNode.leftchild.data:
        rootNode.leftchild=leftRotate(rootNode.leftchild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightchild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightchild.data:
        rootNode.rightchild=rightRotate(rootNode.rightchild)
        return leftRotate(rootNode)
    return rootNode


custAVL = AVLTree(5)
insertNode(custAVL,10)
insertNode(custAVL,4)

levelorderTraversal(custAVL)
































