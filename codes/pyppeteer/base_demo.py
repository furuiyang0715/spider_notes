# pip3 install pyppeteer
# https://blog.csdn.net/lly1122334/article/details/107364106


import os
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


import pyppeteer

# print(pyppeteer.__chromium_revision__)  # 查看版本号
# print(pyppeteer.executablePath())  # 查看 Chromium 存放路径


import pyppeteer.chromium_downloader
print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
# print(pyppeteer.chromium_downloader.chromiumExecutable)

print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('mac')))
print('mac 平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('mac')))
'''
程序首次运行时，会自动下载chromium，但是下载报错，提示ssl错误

[W:pyppeteer.chromium_downloader] start chromium download. Download may take a few minutes. HTTPSConnectionPool(host=‘storage.googleapis.com’, port=443): Max retries exceeded with url: /chromium-browser-snapshots/Win_x64/575458/chrome-win32.zip (Caused by SSLError(SSLError(1, ‘[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:833)’),))
解决办法：打开 /some/path/python3.6/lib/site-packages/pyppeteer/chromium_downloader.py，替换里面DEFAULT_DOWNLOAD_HOST = 'https://storage.googleapis.com’为DEFAULT_DOWNLOAD_HOST = 'http://storage.googleapis.com’即可，具体路径替换成自己的python路径。
————————————————
版权声明：本文为CSDN博主「Louis的日常」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Mr__lqy/article/details/102626025

'''


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://dynamic2.scrape.center/')

    content = await page.content()
    print(content)

    # await page.waitForSelector('.item .name')
    # doc = pq(await page.content())
    # names = [item.text() for item in doc('.item .name').items()]
    # print('Names:', names)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
