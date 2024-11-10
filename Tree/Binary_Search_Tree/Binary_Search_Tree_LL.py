class BSTNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None


custBST=BSTNode(None)


def insertNode(rootNode,nodeValue):
    if rootNode.data==None:
        rootNode.data=nodeValue
    elif rootNode.leftchild>=nodeValue:
        if rootNode.leftchild is None:
            rootNode.data=nodeValue
        else:
            insertNode(rootNode.leftchild,nodeValue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild=nodeValue
        else:
            insertNode(rootNode.rightchild,nodeValue)
    return "The node had been inserted successfully"


