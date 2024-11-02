# we define a node class to initiate each object to the double linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

    # Used to print the values of the node instead of the object location by altering the print function
    def __str__(self):
        return str(self.value)


class Double_Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    # Used to add an element to the linked list
    def append(self,value):
        new_node=Node(value)
        if not self.head:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1

    # used to print all the values by altering print build-in command
    def __str__(self):
        temp_node=self.head
        result=""
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='<->'
            temp_node=temp_node.next
        return result

    # Adding an element to the beginning of the linked list
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1

    # printing all the node values present in the linked list
    def traverse(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.value)
            curr_node=curr_node.next

    # printing all the node values in the reverse order present in the linked list
    def reverse_traverse(self):
        curr_node=self.tail
        while curr_node:
            print(curr_node)
            curr_node=curr_node.prev

    # search for a specific node and send its index
    def search(self,target):
        curr_node=self.head
        index=0
        while curr_node:
            if curr_node.value==target:
                return index
            curr_node=curr_node.next
            index+=1
        return -1

    # used to get the index of the node
    def get(self,index):
        if index<0 or index>=self.length:
            return None
        if index<self.length//2:
            curr_node=self.head
            for _ in range(index):
                curr_node=curr_node.next
        else:
            curr_node=self.tail
            for _ in range(self.length-1,index,-1):
                curr_node=curr_node.prev
        return curr_node

    # Used to set the values of a specific node based on the index value
    def set_value(self,index,value):
        node=self.get(index)
        if node:
            node.value=value
            return True
        return False

    # Used to add a node anywhere in the linked list based on the index of the linked list
    def insert(self,index,value):
        if index<0 or index>self.length:
            print("Index out of range")
            return
        new_node=Node(value)
        if index==0:
            self.prepend(value)
            return
        elif index==self.length:
            self.append(value)
            return
        else:
            temp_node=self.get(index-1)
            new_node.next=temp_node.next
            new_node.prev=temp_node
            temp_node.next.prev=new_node
            temp_node.next=new_node
        self.length+=1

    # Used to remove the first node of the linked list
    def pop_first(self):
        popped_node=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            popped_node.next=None
        self.length-=1
        return popped_node

    # used to remove the last node of the linked list
    def pop(self):
        popped_node=self.tail
        if self.tail==1:
            self.head=None
            self.tail=None

        else:
            self.tail=self.tail.prev
            self.tail.next=None
            popped_node.prev=None
        self.length-=1
        return popped_node

    #Used to remove any node from the linked list based on the index value
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

doublelinkedlist1=Double_Linkedlist()
doublelinkedlist1.append(10)
doublelinkedlist1.append(20)
doublelinkedlist1.append(30)
doublelinkedlist1.append(40)
doublelinkedlist1.append(50)
doublelinkedlist1.append(60)

doublelinkedlist1.insert(5,660)
doublelinkedlist1.set_value(0,100)
doublelinkedlist1.pop()
doublelinkedlist1.remove(4)
print(doublelinkedlist1)





