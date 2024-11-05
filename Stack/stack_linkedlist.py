# Creating a stack using the linkedlist algorithm


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def __iter__(self):
        currNode=self.head
        while currNode:
            yield currNode
            currNode=currNode.next

class Stack:
    def __init__(self):
        self.linkedlist=Linkedlist()

    def __str__(self):
        val=[str(x.value) for x in self.linkedlist]
        return '\n'.join(val)


    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    # Used to insert the element in the stack
    def push(self,value):
        node=Node(value)
        node.next=self.linkedlist.head
        self.linkedlist.head=node

    #Used to remove the first element present in the stack
    def pop(self):
        if self.isEmpty():
            return "There are no elements in the list"
        else:
            nodevalue=self.linkedlist.head.value
            self.linkedlist.head=self.linkedlist.head.next
            return nodevalue

    #Used to retrieve the top most element present in the stack
    def peek(self):
        if self.isEmpty():
            return "There are no current elements present"
        else:
            return self.linkedlist.head.value

    # Used to delete all the elements
    def delete(self):
        self.linkedlist.head=None



custlist=Stack()
custlist.push(12)
custlist.push(13)
custlist.push(14)
print(custlist)
print("-------")
custlist.pop()
print(custlist)
