import asyncio

import aiohttp

from aiohttp import TCPConnector

import time


def test(number):
    start = time.time()

    # async def get(url):
    #     session = aiohttp.ClientSession(connector=TCPConnector(verify_ssl=False))
    #     response = await session.get(url)
    #     await response.text()
    #     await session.close()
    #     return response

    async def get(url):
        async with aiohttp.ClientSession(connector=TCPConnector(verify_ssl=False)) as session:
            response = await session.get(url)
            await response.text()
            return response

    async def request():
        url = 'https://www.baidu.com/'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print('Number:', number, 'Cost time:', end - start)


if __name__ == '__main__':
    for number in [
        # 1, 3, 5, 10, 15,
        # 30, 50, 75, 100,
        200,
        # 500,    # https://www.v2ex.com/t/439254
    ]:
        test(number)


# https://www.javaroad.cn/questions/294085
