import threading
import time

count = 0
lock = threading.Lock()


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global count
        # 获取锁
        lock.acquire()
        temp = count + 1
        time.sleep(0.001)
        count = temp
        # 释放锁
        lock.release()


def main():
    threads = []
    for _ in range(1000):
        thread_ = MyThread()
        thread_.start()
        threads.append(thread_)

    for t in threads:
        t.join()

    print("Final count: ", count)


main()
