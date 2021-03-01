'''
那么你可能会发现，既然 await 后面可以跟一个 coroutine 对象，那么我用 async 把请求的方法改成 coroutine 对象不就可以了吗？所以就改写成如下的样子：
'''

import asyncio
import requests
import time

start = time.time()


async def get(url):
    return requests.get(url)


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
还是不行，它还不是异步执行，也就是说我们仅仅将涉及 IO 操作的代码封装到 async 修饰的方法里面是不可行的！

我们必须要使用支持异步操作的请求方式才可以实现真正的异步，所以这里就需要 aiohttp 派上用场了。

'''
