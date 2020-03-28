import multiprocessing
import time

'''
Semaphore管理一个内置的计数器，
每当调用acquire()时内置计数器-1；
调用release() 时内置计数器+1；
计数器不能小于0；当计数器为0时，acquire()将阻塞线程直到其他线程（进程）调用release()。
'''

buffer = multiprocessing.Queue(10)
empty = multiprocessing.Semaphore(2)   # 缓冲区闲适区空余数
full = multiprocessing.Semaphore(0)    # 缓冲区占用区占用数
lock = multiprocessing.Lock()


class Consumer(multiprocessing.Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()
            buffer.get()
            print("Consumer pop an element.")
            time.sleep(1)
            lock.release()
            empty.release()


class Producer(multiprocessing.Process):
    def __init__(self, name):
        super(Producer, self).__init__()
        self.name = name

    def run(self):
        global buffer, empty, full, lock
        # 生产者 Producer 使用 acquire 方法来占用一个缓冲区位置，缓冲区空闲区大小减 1，接下来进行加锁，对缓冲区进行操作，
        # 然后释放锁，最后让代表占用的缓冲区位置数量加 1，消费者则相反。
        # 通过 Semaphore 我们很好地控制了进程对资源的并发访问数量。
        while True:
            empty.acquire()
            lock.acquire()
            buffer.put(1)
            print(f"{self.name} Producer put an element.")
            time.sleep(1)
            lock.release()
            full.release()


def main():
    lst = []
    for i in range(3):
        p = Producer(str(i))
        p.daemon = True
        p.start()
        lst.append(p)

    c = Consumer()
    c.daemon = True
    c.start()
    c.join()

    for p in lst:
        p.join()

    print("Main End.")


if __name__ == "__main__":
    main()
