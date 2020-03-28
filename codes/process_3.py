import multiprocessing
import time


class MyProcess(multiprocessing.Process):
    def __init__(self, loop):
        super(MyProcess, self).__init__()
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f"Pid: {self.pid}, Name: {self.name}")


def main():
    for i in range(2, 5):
        p = MyProcess(i)
        p.start()


if __name__ == "__main__":
    main()
