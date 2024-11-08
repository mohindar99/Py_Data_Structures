import queue_ds

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

# Creating the node to keep in the BT
drinks = TreeNode("Drinks")
hot=TreeNode("Hot")
cold=TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
alcohol = TreeNode("Alcohol")
NON_alcohol = TreeNode("Non_Alcohol")


# Linking the nodes to the specific rootnodes
drinks.leftchild=hot
drinks.rightchild=cold
hot.leftchild=tea
hot.rightchild=coffee
cold.leftchild=alcohol
cold.rightchild=NON_alcohol


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


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customequeue=queue_ds.Queue()
        customequeue.enqueue(rootNode)
        while not(customequeue.isEmpty()):
            root=customequeue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customequeue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customequeue.enqueue(root.value.rightchild)


def searchBT(rootnode,nodeValue):
    if not rootnode:
        return "The BT does not exists"
    else:
        customequeue = queue_ds.Queue()
        customequeue.enqueue(rootnode)
        while not (customequeue.isEmpty()):
            root = customequeue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftchild is not None:
                customequeue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customequeue.enqueue(root.value.rightchild)

        return "Not Found"


def insertNode(rootnode,newNode):
    if not rootnode:
        rootnode=newNode
    else:
        customequeue = queue_ds.Queue()
        customequeue.enqueue(rootnode)
        while not (customequeue.isEmpty()):
            root = customequeue.dequeue()
            if root.value.leftchild is not None:
                customequeue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild=newNode
            if root.value.rightchild is not None:
                customequeue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild=newNode
        return "Successfully Inserted"



    def getDeepestNode(rootNode):
        if not rootnode:
            return
        else:
            customequeue = queue_ds.Queue()
            customequeue.enqueue(rootNode)
            while not (customequeue.isEmpty()):
                root = customequeue.dequeue()
                print(root.value.data)
                if root.value.leftchild is not None:
                    customequeue.enqueue(root.value.leftchild)
                if root.value.rightchild is not None:
                    customequeue.enqueue(root.value.rightchild)
        deepestNode=root.value
        return deepestNode


    def deleteDeepestNode(rootNode,dnode):
        if not rootNode:
            return
        else:





levelOrderTraversal(drinks)
print(insertNode(drinks,"cola"))