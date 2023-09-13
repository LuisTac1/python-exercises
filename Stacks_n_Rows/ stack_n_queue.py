"""
Stacks and Rows
Stacks - LIFO last in, first out.

Queue - FIFO - first in, first out.
    Example: A bank queue (or any real-life queue)
    queues can have side effects on performance, because with each item changed 
    all indices are modified.
"""

from collections import deque
from time import sleep

queue = deque(maxlen=10)

for i in range(100):
    queue.append(i)
    sleep(1)
    print(queue)
