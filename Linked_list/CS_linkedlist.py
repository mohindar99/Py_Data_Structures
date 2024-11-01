
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class CSLinkedlist:
    # Used to create a circular single linked list of 1 node
    def __init__(self,value):
        new_node=Node(value)
        new_node.next=new_node
        self.head=new_node
        self.tail=new_node
        self.length=1

    # This is the code used to create an empty CSLinked list
    # def __init__(self):
    #     self.head=None
    #     self.tail=None
    #     self.length=0

    # This is the method for the addition of a node to the circular linked list
    def append(self,value):
        new_node=Node(value)
        # if CSLinked list is empty
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        # if the CSLinked list has some elements
        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        self.length+=1


cslinkedlist1=CSLinkedlist(10)

cslinkedlist1.append(10)
cslinkedlist1.append(60)
print(cslinkedlist1.tail.value)