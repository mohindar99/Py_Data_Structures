
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)

class Linkedlist:
     def __init__(self):
         self.head=None
         self.tail=None

     def __iter__(self):
         currnode=self.head
         while currnode:
             yield currnode
             currnode=currnode.next

class Queue:
    def __init__(self):
        self.linkedlist=Linkedlist()

    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return " ".join(values)

    # Adding an element to the queue
    def enqueue(self,value):
        new_node=Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head=new_node
            self.linkedlist.tail=new_node
        else:
            self.linkedlist.tail.next=new_node
            self.linkedlist.tail=new_node


    def isEmpty(self):
        if self.linkedlist.head is None:
            return True
        else:
            return False

    # Removing the element from the queue
    def dequeue(self):
        if self.isEmpty():
            return "There are no elements to dequeue"
        else:
            temp_element=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None

            else:
                self.linkedlist.head=self.linkedlist.head.next
        return temp_element

    # returning the first element of the queue
    def peek(self):
        if self.isEmpty():
            return "There are no elements in the queue to return"
        else:
            return self.linkedlist.head

    def delete(self):
        self.linkedlist.head=None
        self.linkedlist.tail=None



custqueue=Queue()



