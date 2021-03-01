import asyncio


async def execute(x):
    print('Number:', x)


# 定义一个协程对象
coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
# 定义一个事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print('After calling loop')
