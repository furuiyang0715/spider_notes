import threading
import time

now = lambda :time.time()


class MyThread(threading.Thread):
    def __init__(self, interval):
        super(MyThread, self).__init__()
        self.interval = interval

    def run(self):
        name = threading.current_thread().name
        print(f"{name} start")
        time.sleep(self.interval)
        print(f"{name} end")


t1 = now()
print("Main: ", threading.current_thread().name)
for i in range(5):
    thread_instance = MyThread(i)
    thread_instance.start()
    # 可规定主线程在子线程后退出
    if i == 4:
        thread_instance.join()

print(f"Main: end Time: {now() - t1}")
