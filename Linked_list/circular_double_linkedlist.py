from operator import truediv
from webbrowser import open_new


class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

    # Used to print the values of the node instead of the object location by altering the print function
    def __str__(self):
        return str(self.value)


class Circular_Double_Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    #Method to initialise the single node of the linkedlist
    # def __init__(self,value):
    #     new_node=Node(value)
    #     new_node.next=new_node
    #     new_node.prev=new_node
    #     self.head=new_node
    #     self.tail=new_node
    #     self.length+=1

    # used to add an node in the end
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.pre=new_node
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.prev=self.tail
            new_node.next=self.head
            self.tail=new_node
        self.length+=1

    def __str__(self):
        current_node=self.head
        result=''
        while current_node:
            result+=str(current_node.value)
            current_node=current_node.next
            if current_node==self.head:
                break
            result+='<->'
        return result

    # used to add a node in the beginning of the list
    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
            new_node.next=new_node
            new_node.prev=new_node
        else:
            self.tail.next=new_node
            self.head.prev=new_node
            new_node.next=self.head
            new_node.prev=self.tail
            self.head=new_node
        self.length+=1

    # Used to print all the node values of the list
    def traverse(self):
        curr=self.head
        while curr:
            print(curr.value)
            curr=curr.next
            if curr==self.head:
                break

    # Used to print all the values in reverse order
    def reverse_traverse(self):
        curr=self.tail
        while curr:
            print(curr)
            curr=curr.prev
            if curr==self.tail:
                break

    #used to search a value in the list and return bool based on the result
    def search(self,target):
        curr=self.head
        while curr:
            if curr.value==target:
                return True
            curr=curr.next
            if curr==self.head:
                break
        return False

    # Used to the index node address based on the index
    def get(self,index):
        curr=None
        if index<0 or index>=self.length:
            return None

        if index<self.length//2:
            curr=self.head
            for i in range(index):
                curr=curr.next

        else:
            curr=self.tail
            for i in range(self.length-1,index,-1):
                curr=curr.prev
        return curr

    # used to update the value of the list based on the index values
    def set(self,index,value):
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    # used to insert the node in a specific position based on the index
    def insert(self,index,value):
        if index<0 or index >self.length:
            print("Index out of bounce")
            return
        if index==0:
            self.prepend(value)
            return
        if index==self.length:
            self.append(value)
            return
        new_node=Node(value)
        temp_node=self.get(index)
        new_node.next=temp_node.next
        new_node.prev=temp_node
        temp_node.next.prev=new_node
        temp_node.next=new_node
        self.length+=1

    #Used to remove the first element of the list
    def pop_first(self):
        if self.length==0:
            return None
        popped_node=self.head
        if self.head==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            popped_node.prev=None
            popped_node.next=None
            self.head.prev=self.tail
            self.tail.next=self.head
        self.length-=1
        return popped_node

    # Used to remove the last node of the list
    def pop(self):
        if self.length==0:
            return None
        popped_node=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            popped_node.next=None
            popped_node.prev=None
            self.tail.next=self.head
            self.head.prev=self.tail
        self.length-=1
        return popped_node

    # Used to remove the specific node from a specific index
    def remove(self,index):
        if index<0 or index>=self.length:
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        popped_node=self.get(index)
        popped_node.prev.next=popped_node.next
        popped_node.next.prev=popped_node.prev
        popped_node.next=None
        popped_node.prev=None
        self.length-=1
        return popped_node

    # Used to delete all the nodes present  in the list
    def delete_all(self):
        self.head=None
        self.tail=None
        self.length=0


cdll1=Circular_Double_Linkedlist()
cdll1.append(10)
cdll1.append(20)
cdll1.append(30)
cdll1.prepend(45)
print(cdll1)
cdll1.remove(1)
print(cdll1)