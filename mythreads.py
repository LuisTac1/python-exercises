"""
Threads - Running processing
"""
from time import sleep
from threading import Thread
from threading import Lock


# Thread
class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


t1 = MyThread('Thread 1', 5)
t1.start()

t2 = MyThread('Thread 2', 3)
t2.start()

t3 = MyThread('Thread 3', 2)
t3.start()

for i in range(20):
    print(i)
    sleep(1)


# Ticket purchase example
class Tickets:
    def __init__(self, stock):
        self.stock = stock
        self.lock = Lock()

    def purchase(self, amount):
        self.lock.acquire()

        if self.stock < amount:
            print('Dont have enough tickets.')
            self.lock.release()
            return

        sleep(1)

        self.stock -= amount
        print(f'You bought {amount} ticket(s), still has {self.stock}')

        self.lock.release()


if __name__ == '__main__':
    tickets = Tickets(10)

    threads = []

    for i in range(1, 6):
        t = Thread(target=tickets.purchase, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    running = True
    while running:
        running = False
        for t in threads:
            if t.is_alive():
                running = True
                break

    print('Tickets in stock: ', tickets.stock)
