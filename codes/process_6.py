import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def __init__(self, loop, lock: multiprocessing.Lock):
        super(MyProcess, self).__init__()
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print(f"Pid: {self.pid}, LoopCount: {count}")
            self.lock.release()


def main():
    lock = multiprocessing.Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()


if __name__ == "__main__":
    main()
