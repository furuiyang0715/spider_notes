import multiprocessing


class Consumer(multiprocessing.Process):
    def __init__(self, pipe):
        super(Consumer, self).__init__()
        self.pipe = pipe

    def run(self):
        self.pipe.send("Consumer Words.")
        print(f"Consumer Recv: {self.pipe.recv()}")


class Producer(multiprocessing.Process):
    def __init__(self, pipe):
        super(Producer, self).__init__()
        self.pipe = pipe

    def run(self):
        self.pipe.send("Producer Words.")
        print(f"Producer Recv: {self.pipe.recv()}")


def main():
    # 声明了一个默认为双向的管道，然后将管道的两端分别传给两个进程。
    # 管道 Pipe 就像进程之间搭建的桥梁，利用它我们就可以很方便地实现进程间通信了。
    pipe = multiprocessing.Pipe()
    c = Consumer(pipe[0])
    p = Producer(pipe[1])
    c.daemon = True
    p.daemon = True
    c.start()
    p.start()
    c.join()
    p.join()
    print("Main Process Ended.")


if __name__ == "__main__":
    main()
