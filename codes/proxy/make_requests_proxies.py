import requests

proxy = '127.0.0.1:7890'
proxies = {'http': 'http://'+proxy,
           'https': 'https://'+proxy
           }

try:
    response = requests.get('https://httpbin.org/get',
                            # proxies=proxies,    # 切换是否使用代理
                            )
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)


# 运行结果：
#
# {
#
#  "args": {},
#
#  "headers": {
#
#    "Accept": "*/*",
#
#    "Accept-Encoding": "gzip, deflate",
#
#    "Host": "httpbin.org",
#
#    "User-Agent": "python-requests/2.22.0",
#
#    "X-Amzn-Trace-Id": "Root=1-5e8f358d-87913f68a192fb9f87aa0323"
#
#  },
#
#  "origin": "210.173.1.204",
#
#  "url": "https://httpbin.org/get"
#
# }


# 在代理需要进行持续认证时的写法: proxy = 'username:password@127.0.0.1:7890'
