import asyncio
import aiohttp
proxy = 'http://127.0.0.1:7890'


# 设置认证代理: proxy = 'http://username:password@127.0.0.1:7890'
async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', proxy=proxy) as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())


# pip3 install aiohttp-socks
import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector

connector = ProxyConnector.from_url('socks5://127.0.0.1:7891')


async def main():
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get('https://httpbin.org/get') as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
