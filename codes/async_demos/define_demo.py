import asyncio


async def execute(x):
    print('Number:', x)


'''
可见，async 定义的方法就会变成一个无法直接执行的 coroutine 对象，必须将其注册到事件循环中才可以执行。
上面我们还提到了 task，它是对 coroutine 对象的进一步封装，它里面相比 coroutine 对象多了运行状态，比如 running、finished 等，我们可以用这些状态来获取协程对象的执行情况。
在上面的例子中，当我们将 coroutine 对象传递给 run_until_complete 方法的时候，实际上它进行了一个操作就是将 coroutine 封装成了 task 对象. 
'''
# # 定义一个协程对象
# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
# # 定义一个事件循环
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('After calling loop')


# coroutine = execute(1)
# print('Coroutine:', coroutine)
# print('After calling execute')
# loop = asyncio.get_event_loop()
# # 显式创建一个 task 对象
# task = loop.create_task(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')


coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')
task = asyncio.ensure_future(coroutine)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')
