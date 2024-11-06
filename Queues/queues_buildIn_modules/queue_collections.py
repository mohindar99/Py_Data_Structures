# Using the queues with the in build-collections keywords:

from collections import deque

custqueue = deque(maxlen=3)

custqueue.append(23)
custqueue.append(24)
custqueue.append(35)
custqueue.append(35)
print(custqueue)
custqueue.popleft()
print(custqueue)