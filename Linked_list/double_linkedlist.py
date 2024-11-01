
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

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

    def __str__(self):
        temp_node=self.head
        result=""
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='<->'
            temp_node=temp_node.next
        return result

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


    def traverse(self):
        curr_node=self.head
        while curr_node:
            print(curr_node.value)
            curr_node=curr_node.next

    def reverse_traverse(self):
        curr_node=self.tail
        while curr_node:
            print(curr_node)
            curr_node=curr_node.prev

    def search(self,target):
        curr_node=self.head
        index=0
        while curr_node:
            if curr_node.value==target:
                return index
            curr_node=curr_node.next
            index+=1
        return -1

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




doublelinkedlist1=Double_Linkedlist()
doublelinkedlist1.append(10)
doublelinkedlist1.append(20)
doublelinkedlist1.append(30)
doublelinkedlist1.prepend(60)

print(doublelinkedlist1)
print(doublelinkedlist1.get(1))




