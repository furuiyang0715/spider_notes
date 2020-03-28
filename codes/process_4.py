import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def __init__(self, loop):
        super(MyProcess, self).__init__()
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f"Loop: {self.loop}, Pid: {self.pid}, Loop Count: {count}")


def main():
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()


if __name__ == "__main__":
    main()


# 主进程没有做任何事情 直接输入后结束 同时也终止了子进程的运行。
print("Main End.")
