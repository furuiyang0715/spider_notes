import threading
import time


now = lambda :time.time()


def work(internal):
    name = threading.current_thread().name
    print(f"{name} start")
    time.sleep(internal)
    print(f"{name} end")


t1 = now()
print("Main: ", threading.current_thread().name)
for i in range(5):
    thread_instance = threading.Thread(target=work, args=(i, ))
    thread_instance.start()
    # 可规定主线程在子线程后退出
    if i == 4:
        thread_instance.join()

print(f"Main: end, Time: {now() - t1}")
