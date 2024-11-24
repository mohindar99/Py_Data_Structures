# Here we are creating a counter using the iterator methods

class Counter:
    def __init__(self,limit):
        self.num=1
        self.limit=limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<self.limit:
            val=self.num
            self.num+=1
            return val
        else: raise StopIteration

values=Counter(12)
for i in values:
    print(i)