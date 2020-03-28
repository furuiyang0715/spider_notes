import multiprocessing
import requests


def scrape(url):
    try:
        ret = requests.get(url).text
        print(ret[:10])
        print()
    except:
        print("Get Error")


def main():
    pool = multiprocessing.Pool(processes=3)
    urls = [
        'http://data.eastmoney.com/hsgt/index.html',
        'http://data.eastmoney.com/hsgtcg/gzcglist.html',
        'https://www.runoob.com/mysql/mysql-alter.html',
        'https://blog.csdn.net/weixin_42329277/article/details/80735009?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task',

    ]
    pool.map(scrape, urls)
    pool.close()
    # pool.join()
    print("Main End.")


if __name__ == "__main__":
    main()
