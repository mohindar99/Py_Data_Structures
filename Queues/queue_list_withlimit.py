# Here we are creating the circular queue in order to decrease the time complexity

class Queue:
    def __init__(self,maxsize):
        self.items=[None]*maxsize
        self.maxsize=maxsize
        self.start=-1
        self.top=-1

    def __str__(self):
        values=[str(x) for x in self.items]
        return " ".join(values)

    # used to check the queue is full or not
    def isFull(self):
        if self.top+1==self.start:
            return True

        elif self.start==0 and self.top+1==self.maxsize:
            return True

        else:
            return False

    # Used to check if the queue is empty or not
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False


    # It is used to insert an element in the queue

    def Enqueue(self,value):
        if self.isFull():                                       # Check weather the queue is full or not
            return "The queue is Full"
        else:
            if self.top+1==self.maxsize:                        # check if the top value is in the end of the queue
                self.top=0
            else:
                self.top+=1                                     # If not in the end then it would be somewhere in the middle
                if self.start==-1:                              # If the start element is -1 like adding the first element in the queue then
                    self.start=0                                # update the start value as well
            self.items[self.top]=value
            return "The element is added successfully"


    # It is used to remove an element from the queue based on the order
    def Dequeue(self):
        if self.isEmpty():
            return "The list is empty"

        else:
            firstelement=self.items[self.start]
            start=self.start
            if self.start==self.top:                          # If there is only 1 element in the list
                self.start=-1
                self.top=-1
            elif self.start+1==self.maxsize:                  # If the queue reaches to the end
                self.start=0
            else:                                             # If the start is present in the middle and top is in the end
                self.start+=1

            self.items[start]=None
            return firstelement

    # used to check the first value of the queue
    def peek(self):
        if self.isEmpty():
            return "There are no elements to return in the queue"
        else:
            return self.items[self.start]

    # Used to remove all the elements from the queue
    def delete(self):
        self.items=self.maxsize*[None]
        self.top=-1
        self.start=-1


custqueue=Queue(6)
custqueue.Enqueue(1)
custqueue.Enqueue(2)
custqueue.Enqueue(3)
custqueue.Enqueue(4)
custqueue.Enqueue(56)
custqueue.Enqueue(45)
print(custqueue)
custqueue.Dequeue()
custqueue.Dequeue()
print(custqueue)
print(custqueue.peek())










