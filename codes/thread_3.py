import threading
import time


now = lambda:time.time()


def work(internal):
    name = threading.current_thread().name
    print(f"{name} start")
    time.sleep(internal)
    print(f"{name} end")


thread_1 = threading.Thread(target=work, args=(1, ))
thread_2 = threading.Thread(target=work, args=(5, ))
thread_2.setDaemon(True)
thread_1.start()
thread_2.start()

print("Main End.")
