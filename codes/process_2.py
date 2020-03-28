import multiprocessing
import time

now = lambda: time.time()


def work(index):
    print(index)
    time.sleep(index)


def main():
    start_dt = now()
    for i in range(5):
        p = multiprocessing.Process(target=work, args=(i,))
        p.start()

    # 查看本机的 cpu 数量
    print(f"CPU Numbers: {multiprocessing.cpu_count()}")
    # 查看全部活跃子进程的名称以及pid
    for p in multiprocessing.active_children():
        print(p.name, p.pid)

    print(f"Time End: {now() - start_dt}")


if __name__ == "__main__":
    main()
