from bdb import Breakpoint


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    # This method would help in printing the value of a object if it is called by the object
    def __str__(self):
        return str(self.value)


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

    # In build method which is called when the print operation is used so we have modified it
    def __str__(self):
        temp_node=self.head
        result=" "
        while temp_node is not None:
            result+=str(temp_node.value)
            temp_node=temp_node.next
            if temp_node == self.head:
                break
            result += "->"
        return result

    # Method to prepend the node in the beginning of the element
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=new_node
        self.length+=1


    # This method is used to insert a specific element in a specific position based on the index of it.
    def insert(self,index,value):
        new_node=Node(value)
        if index>self.length or index<0:
            raise Exception("Index out of range")

        if index==0:
            # index insertion of an empty list
            if self.length==0:
                self.head=new_node
                self.tail=new_node
                new_node.next=new_node
            # index insertion of a node which has some elements and want to insert at index=0
            else:
                new_node.next=self.head
                self.head=new_node
                self.tail.next=new_node
        # insertion at the end of the list
        elif index==self.length:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        # insertion at the middle of the list
        else:
            temp_node=self.head
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1

    # This method is used to print all the values of the CSLinked list
    def traverse(self):
        current=self.head
        while current is not None:
            print(current.value)
            current=current.next
            if current == self.head:
                break

    # This method is used to search an element from the circular list
    def search(self,target):
        current=self.head
        while current is not None:
            if current.value==target:
                return True
            current=current.next
            if current==self.head:
                break
        return False

    # This will return the address of the object based on the index value
    def get(self,index):
        if index==-1:
            return self.tail
        elif index<-1 or index>self.length:
            return None
        current=self.head
        for _ in range(index):
            current=current.next
        return current

    # This method is used to update the values of the linkedlist based on the index and value provided by user
    def set_values(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    # In this method we would remove the first node of the CSLinked list
    def pop_first(self):
        popped_node =self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
            popped_node.next=None
        self.length-=1
        return popped_node

    # It is used to remove the last node of the CSLinked list
    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if self.length==1:
            self.head=self.tail=None
        else:
            temp=self.head
            while temp is not self.tail:
                temp=temp.next
            temp.next=self.head
            self.tail=temp
            popped_node.next=None
        self.length-=1
        return popped_node

    #It is used to remove the element based on the index of the value
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        elif index==0:
            return self.pop_first()
        elif index==self.length-1:
            return self.pop()
        prev_node = self.get(index-1)
        popped_node=prev_node.next
        prev_node.next=popped_node.next
        popped_node.next=None
        self.length-=1
        return popped_node

    # Used to remove all the element of the circular linked list
    def delete_all(self):
        if self.length==0 : return
        self.tail.next=None
        self.head=self.tail=None
        self.length=0


cslinkedlist1=CSLinkedlist(10)
cslinkedlist1.append(10)
cslinkedlist1.append(60)
cslinkedlist1.prepend(450)
cslinkedlist1.insert(1,23)
cslinkedlist1.insert(0,24)
print(cslinkedlist1)
print(cslinkedlist1.set_values(2,34))
print(cslinkedlist1)
cslinkedlist1.pop_first()
print(cslinkedlist1)
print(cslinkedlist1.remove(2))
print(cslinkedlist1)
print(cslinkedlist1.delete_all())
print(cslinkedlist1.tail)