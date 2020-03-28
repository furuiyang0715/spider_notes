import multiprocessing
import time


def function(index):
    print(f"{index} start")
    time.sleep(3)
    print(f"{index} end")


def main():
    # 声明了一个大小为 3 的进程池，通过 processes 参数来指定，如果不指定，那么会自动根据处理器内核来分配进程数。
    pool = multiprocessing.Pool(processes=3)
    for i in range(4):
        # 使用 apply_async 方法将进程添加进去，args 可以用来传递参数。
        pool.apply_async(function, args=(i, ))

    print("Main start.")
    # 关闭进程池 使之不再接受新任务
    pool.close()
    pool.join()
    print("Main end.")


if __name__ == "__main__":
    main()
