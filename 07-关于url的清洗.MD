1. URL清洗
网络请求开始之前，先把url清洗一遍，可以避免重复下载、无效下载（二进制内容），节省服务器和网络开销。

2. cchardet 模块
该模块是chardet的升级版，功能和chardet完全一样，用来检测一个字符串的编码。由于是用C和C++实现的，所以它的速度非常快，
非常适合在爬虫中用来判断网页的编码。
切记，不要相信requests返回的encoding，自己判断一下更放心。 

3. traceback 模块
我们写的爬虫在运行过程中，会出现各种异常，而且有些异常是不可预期的，也不知道它会出现在什么地方，我们就需要用try来捕获异常让程序不中断，
但是我们又需要看看捕获的异常是什么内容，由此来改善我们的爬虫。这个时候，就需要traceback模块。
用traceback.print_exc()来输出异常，有助于我们发现更多问题。

清洗新闻类的url 的模块实例代码：

```python
import urllib.parse as urlparse 
# 判断是否为二进制内容路径后缀
g_bin_postfix = set([
    'exe', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
    'pdf',
    'jpg', 'png', 'bmp', 'jpeg', 'gif',
    'zip', 'rar', 'tar', 'bz2', '7z', 'gz',
    'flv', 'mp4', 'avi', 'wmv', 'mkv',
    'apk',
])

# 静态文件标志 
g_news_postfix = [
    '.html?', '.htm?', '.shtml?',
    '.shtm?',
]


def clean_url(url):
    # 1. 是否为合法的http url， 非法的 url 直接返回空
    if not url.startswith('http'):
        return ''
    # 2. 去掉静态化url后面的参数 就是去掉 ? 后面的内容
    # ?后面的内容 例如: http://xinwen.eastday.com/a/n181106070849091.html?qid=news.baidu.com
    # 或者是 http://news.ifeng.com/a/20181106/60146589_0.shtml?_zbs_baidu_news
    # 一般是与新闻门户的网站的目标导向网站做流量分析使用的
    for np in g_news_postfix:
        p = url.find(np)
        if p > -1:
            p = url.find('?')
            url = url[:p]
            return url

    # 3. 不下载二进制类内容的链接
    up = urlparse.urlparse(url)
    path = up.path
    if not path:
        path = '/'
    postfix = path.split('.')[-1].lower()
    if postfix in g_bin_postfix:
        return ''

    # 4. 去掉标识流量来源的参数
    # 去掉不要的参数之后重新拼接
    # badquery = ['spm', 'utm_source', 'utm_source', 'utm_medium', 'utm_campaign']
    good_queries = []
    for query in up.query.split('&'):
        qv = query.split('=')
        if qv[0].startswith('spm') or qv[0].startswith('utm_'):
            continue
        if len(qv) == 1:
            continue
        good_queries.append(query)
    # 将剩余的请求重新拼接
    # TODO 或许需要对请求参数的顺序进行排序 才能完全判断实质是同一个 url
    query = '&'.join(good_queries)
    url = urlparse.urlunparse((
        up.scheme,
        up.netloc,
        path,
        up.params,
        query,
        ''  #  crawler do not care fragment
    ))
    return url
``` 
