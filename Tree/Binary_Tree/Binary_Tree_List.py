from sys import maxsize


class BinaryTree:
    def __init__(self,size):
        self.customList=[None]*size
        self.lastusedindex = 0
        self.maxSize=size

    def insert(self,value):
        if self.lastusedindex+1==maxsize:
            return "The list is out of range"
        self.customList[self.lastusedindex+1]=value
        self.lastusedindex+=1
        return "The value is inserted successfully"

    def search(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i]==nodeValue:
                return "Success"
        return "Not found"

    def preorderTraversal(self,Index):
        if Index>self.lastusedindex:
            return
        print(self.customList[Index])
        self.preorderTraversal(Index*2)
        self.preorderTraversal(Index*2+1)

    def inorderTraversal(self,Index):
        if Index>self.lastusedindex:
            return
        self.preorderTraversal(Index*2)
        print(self.customList[Index])
        self.preorderTraversal(Index*2+1)

    def postorderTraversal(self,Index):
        if Index>self.lastusedindex:
            return
        print(self.customList[Index])
        self.preorderTraversal(Index*2)
        self.preorderTraversal(Index*2+1)
        print(self.customList[Index])

    def levelorderTraversal(self,index):
        for i in range(index,self.lastusedindex+1):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastusedindex==0:
            return "There is no node to delete"
        for i in range(1,self.lastusedindex+1):
            if self.customList[i]==value:
                self.customList[i]=self.customList[self.lastusedindex]
                self.customList[self.lastusedindex]=None
                self.lastusedindex-=1
        return "The node had been deleted"


    def deleteall(self):
        self.customList=None
        return "The entire BT had been deleted"


newBT=BinaryTree(8)
newBT.insert(21)
newBT.insert(22)
newBT.insert(23)
newBT.insert(24)
print(newBT.search(24))
