from multiprocessing import Queue

custqueue=Queue(maxsize=3)
custqueue.put(1)
custqueue.put(2)
custqueue.put(3)


print(custqueue)