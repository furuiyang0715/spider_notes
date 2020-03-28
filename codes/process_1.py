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

    print(f"Time: {now() - start_dt}")


if __name__ == "__main__":
    main()
