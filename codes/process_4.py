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
    processes = []
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()
        processes.append(p)

    for p in processes:
        # 主进程最多等待改进程 1 s
        p.join(1)


if __name__ == "__main__":
    main()


# 主进程没有做任何事情 直接输入后结束 同时也终止了子进程的运行。
print("Main End.")
