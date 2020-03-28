import threading
import time

count = 0


class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global count
        temp = count + 1
        time.sleep(0.001)
        count = temp


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
