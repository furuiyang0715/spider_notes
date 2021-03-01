import time
import asyncio
import requests


# async def request():
#     url = 'https://www.baidu.com'
#     time.sleep(4)
#     status = requests.get(url)
#     return status

# t1 = time.time()
# tasks = [asyncio.ensure_future(request()) for _ in range(5)]
# print('Tasks:', tasks)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# for task in tasks:
#     print('Task Result:', task.result())
# print(time.time() - t1)



'''
这次它遇到 await 方法确实挂起了，也等待了，但是最后却报了这么个错，
TypeError: object Response can't be used in 'await' expression
这个错误的意思是 requests 返回的 Response 对象不能和 await 一起使用，为什么呢？因为根据官方文档说明，await 后面的对象必须是如下格式之一：
A native coroutine object returned from a native coroutine function，一个原生 coroutine 对象。
A generator-based coroutine object returned from a function decorated with types.coroutine，一个由 types.coroutine 修饰的生成器，这个生成器可以返回 coroutine 对象。
An object with an __await__ method returning an iterator，一个包含 __await__ 方法的对象返回的一个迭代器。
'''


async def request():
    url = 'https://static4.scrape.center/'
    print('Waiting for', url)
    response = await requests.get(url)
    print('Get response from', url, 'response', response)


t1 = time.time()
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print('Tasks:', tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print('Task Result:', task.result())
print(time.time() - t1)
