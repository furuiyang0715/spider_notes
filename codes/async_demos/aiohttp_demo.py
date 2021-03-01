# 官方文档链接为：https://aiohttp.readthedocs.io/，它分为两部分，一部分是 Client，一部分是 Server，详细的内容可以参考官方文档。

import asyncio

import aiohttp

import time

start = time.time()


async def get(url):
    session = aiohttp.ClientSession()
    response = await session.get(url)
    await response.text()
    await session.close()
    return response


async def request():
    url = 'https://static4.scrape.center/'
    print('Waiting for', url)
    response = await get(url)
    print('Get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('Cost time:', end - start)


'''
代码里面我们使用了 await，后面跟了 get 方法，在执行这 10 个协程的时候，如果遇到了 await，那么就会将当前协程挂起，
转而去执行其他的协程，直到其他的协程也挂起或执行完毕，再进行下一个协程的执行。

开始运行时，时间循环会运行第一个 task，针对第一个 task 来说，当执行到第一个 await 跟着的 get 方法时，它被挂起，
但这个 get 方法第一步的执行是非阻塞的，挂起之后立马被唤醒，所以立即又进入执行，创建了 ClientSession 对象，
接着遇到了第二个 await，调用了 session.get 请求方法，然后就被挂起了，由于请求需要耗时很久，所以一直没有被唤醒。

当第一个 task 被挂起了，那接下来该怎么办呢？事件循环会寻找当前未被挂起的协程继续执行，于是就转而执行第二个 task 了，
也是一样的流程操作，直到执行了第十个 task 的 session.get 方法之后，全部的 task 都被挂起了。所有 task 都已经处于挂起状态，怎么办？只好等待了。

5 秒之后，几个请求几乎同时都有了响应，然后几个 task 也被唤醒接着执行，输出请求结果，最后总耗时，6 秒！
怎么样？这就是异步操作的便捷之处，当遇到阻塞式操作时，任务被挂起，程序接着去执行其他的任务，而不是傻傻地等待，这样可以充分利用 CPU 时间，而不必把时间浪费在等待 IO 上。

你可能会说，既然这样的话，在上面的例子中，在发出网络请求后，既然接下来的 5 秒都是在等待的，在 5 秒之内，CPU 可以处理的 task 数量远不止这些，
那么岂不是我们放 10 个、20 个、50 个、100 个、1000 个 task 一起执行，最后得到所有结果的耗时不都是差不多的吗？因为这几个任务被挂起后都是一起等待的。

理论来说确实是这样的，不过有个前提，那就是服务器在同一时刻接受无限次请求都能保证正常返回结果，也就是服务器无限抗压，
另外还要忽略 IO 传输时延，确实可以做到无限 task 一起执行且在预想时间内得到结果。
但由于不同服务器处理的实现机制不同，可能某些服务器并不能承受这么高的并发，因此响应速度也会减慢。

'''
