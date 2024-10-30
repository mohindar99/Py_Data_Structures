# This is the node class where we use to create each node by its data and address
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

# Linked list for the total number of node's 1
# class LinkedlistSingleElement:
#     def __init__(self,value):
#         new_node=Node(value)
#         self.head=new_node
#         self.tail=new_node
#         self.length=1

# Linked list for the total number of '0' node

class EmptyLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    # adding an element at the end of the linked list which is called append
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    # Used to print the values of the linked list while using the print statement.
    def __str__(self):
        temp_node=self.head
        result=' '

        while temp_node is not None:
            result+= str(temp_node.value)
            if temp_node.next is not None:
                result+= '->'
            temp_node=temp_node.next

        return result

    # This method is used to add an element in the beginning of linkedlist by checking the conditions

    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node

        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

# we are trying to insert a element in a specific index of the linked list
    def insert(self,index,value):
        new_node = Node(value)
        # return false if the index is less than 0 and index is out of range
        if index<0 or index>self.length:
            return False

        # operation to do when the linkedlist is empty and. you want to insert element
        elif self.length==0:
            self.head=new_node
            self.tail=new_node

        # operation to do when you want to insert an element in the index 0 of the liked list which has values
        # as it is not possible because we are loping from the next value
        elif index==0:
            new_node.next=self.head
            self.head=new_node

        # operation to do when you are adding an element in the middle of the linked list
        else:
            temp_node=self.head
            for i in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
            self.length+=1

        return True






new_linkedlist=EmptyLinkedlist()

new_linkedlist.append(10)
new_linkedlist.append(20)
new_linkedlist.prepend(500)

# In this way we fetch the values of the linkedlist
# print(new_linkedlist.head)
# print(new_linkedlist.tail)

print(new_linkedlist)