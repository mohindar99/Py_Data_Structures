
class Stack:
    def __init__(self,maxsize):
        self.list=[]
        self.maxsize=maxsize

    # Used to print the custom elements
    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return '\n'.join(values)

    # Used to check if the elements in the stack are none or not
    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    # This method is used to check the current size of the list that it is full or not
    def isFull(self):
        if len(self.list)==self.maxsize:
            return True
        else:
            return False

    # Used to push an element to the stack based on the max size of the stack
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            return self.list.append(value)

    # Usd to remove a specific element from the list
    def pop(self):
        if self.isEmpty():
            return "no element to remove"
        else:
            return self.list.pop()

    # Used to get a small peek of the first element of the stack
    def peek(self):
        if self.isEmpty():
            return "There are no elements in the list"
        else:
            return self.list[len(self.list)-1]

    # Used to delete all the elements from the stack
    def delete(self):
        self.list=None


custStack=Stack(5)
custStack.push(1)
custStack.push(2)
custStack.push(3)
custStack.push(4)
print(custStack)



