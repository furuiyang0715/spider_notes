import multiprocessing
import time


def task():
    print("1")
    time.sleep(5)
    print("2")


if __name__ == "__main__":
    p = multiprocessing.Process(target=task)
    # 使用 is_alive 判断当前进程进程是否在运行
    print(f"First: {p}, {p.is_alive()}")

    p.start()
    print(f"During: {p}, {p.is_alive()}")

    p.terminate()
    # 即使此时已经调用了 terminate 进程的状态还是 True, 即运行状态
    # 在调用 join 之后才变成了终止状态
    print(f"After: {p}, {p.is_alive()}")

    p.join()
    print(f"Joined: {p}, {p.is_alive()}")
