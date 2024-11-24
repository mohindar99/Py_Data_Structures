# importing queue from the build in modules
import queue as q

# Some of the operations which are performed on the queue of FIFO
customequeue=q.Queue(maxsize=3)
print(customequeue.empty())
customequeue.put(1)
customequeue.put(2)
customequeue.put(3)
print(customequeue.full())
print(customequeue.get())
print(customequeue.qsize())