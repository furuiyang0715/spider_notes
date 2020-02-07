### 使用说明 
```python
# 测试一个生成伪装请求头的模块
from fake_useragent import UserAgent
ua = UserAgent()
# 查看 ua 的属性
attrs = [attr for attr in dir(ua) if not attr.startswith("_")]
# print(attrs)
# ['cache', 'data', 'data_browsers', 'data_randomize', 'fallback', 'load', 'path',
# 'safe_attrs', 'update', 'use_cache_server', 'verify_ssl']

# 创建 ie 浏览器的请求头
ie_agent = ua.ie
print(ie_agent)  # Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)
# 创建 opera 浏览器的请求头
print(ua.opera)
# Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01
# 创建 firefox 浏览器的请求头
print(ua.firefox)
# Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0
# 创建 safari 浏览器的请求头
print(ua.safari)
# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A

# 随机生成请求头 最实用的功能
rua = ua.random
print(rua)

# 在爬虫程序中的具体使用套路
import requests
from fake_useragent import UserAgent
ua = UserAgent()
headers = {"User-Agent": ua.random}
demo_url = "https://wwww.baidu.com"
ret = requests.get(demo_url, headers=headers)
print(ret)

```
