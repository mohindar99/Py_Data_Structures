#This is a stack which was created based on the list without any limit to the stack .

class Stack:
    def __init__(self):
        self.list=[]

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

    # Used to send some elements to the list
    def push(self,value):
        self.list.append(value)
        return "The value is inserted successfully"

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



stack1=Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1)
print(stack1.peek())

