from unittest.mock import right


class Heap:
    def __init__(self,size):
        self.customList=(size+1) * [None]
        self.heapSize=0
        self.maxSize=size+1

def peekofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customeList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize


def levelorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapSize+1):
            print(rootNode.customList[i])


def heapifyTreeNode(rootNode,index,heapType):
    parentIndex=int(index/2)
    if index<=1:
        return
    if heapType=="Min":
        if rootNode.customList[index]<rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeNode(rootNode,parentIndex,heapType)
    elif heapType=='Max':
        if rootNode.customList[index]>rootNode.customList[parentIndex]:
            temp=rootNode.customList[index]
            rootNode.customList[index]=rootNode.customList[parentIndex]
            rootNode.customList[parentIndex]=temp
        heapifyTreeNode(rootNode,parentIndex,heapType)
    return "The value had been inserted successfully"

def insertNode(rootNode,nodeValue,heaptype):
    if rootNode.heapSize+1==rootNode.maxSize:
        return "The heap is full"
    rootNode.customList[rootNode.heapSize+1]=nodeValue
    rootNode.heapSize+=1
    heapifyTreeNode(rootNode,rootNode.heapSize,heaptype)
    return "The value is inserted"


def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex=index*2
    rightIndex=(index*2)+1
    swapchild=0

    if rootNode.heapSize<leftIndex:
        return
    elif rootNode.heapSize==leftIndex:
        if heapType=='Min':
            if rootNode.customList[index]>rootNode.customList[leftIndex]:
                temp=rootNode.customList[index]
                rootNode.customList[index]=rootNode.customList[leftIndex]
                rootNode.customList[leftIndex]=temp
        elif heapType=="Max":
            if rootNode.customList[index]<rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
    else:
        if heapType=="Min":
            if rootNode.customList[leftIndex]<rootNode.customList[rightIndex]:
                swapchild=leftIndex
            else:
                swapchild=rightIndex
            if rootNode.customList[swapchild]<rootNode.customList[index]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapchild]
                rootNode.customList[swapchild] = temp
        elif heapType=="Max":
            if rootNode.customList[leftIndex]>rootNode.customList[rightIndex]:
                swapchild=leftIndex
            else:
                swapchild=rightIndex
            if rootNode.customList[swapchild]>rootNode.customList[index]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapchild]
                rootNode.customList[swapchild] = temp
        heapifyTreeExtract(rootNode,swapchild,heapType)


def extractNode(rootNode,heapType):
    if rootNode.heapSize==0:
        return
    ExtractedNode=rootNode.customList[1]
    rootNode.customList[1]=rootNode.customList[rootNode.heapSize]
    rootNode.customList[rootNode.heapSize]=None
    rootNode.heapSize-=1
    heapifyTreeExtract(rootNode,1,heapType)
    return ExtractedNode



custHeap=Heap(5)
insertNode(custHeap,4,"Max")
insertNode(custHeap,5,"Max")
insertNode(custHeap,2,"Max")
insertNode(custHeap,1,"Max")
print(extractNode(custHeap,"Max"))
print("Nine")
levelorderTraversal(custHeap)