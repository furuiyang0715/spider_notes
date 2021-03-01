# import requests
#
# proxy = '127.0.0.1:7891'
#
# proxies = {
#     'http': 'socks5://'+proxy,
#     'https': 'socks5://'+proxy
# }
#
# try:
#     response = requests.get('https://httpbin.org/get',
#                             # proxies=proxies,
#                             )
#     print(response.text)
# except requests.exceptions.ConnectionError as e:
#     print('Error', e.args)


# pip3 install "requests[socks]"


import requests
import socks     # 无法安装
import socket
socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 7891)
socket.socket = socks.socksocket

try:
    response = requests.get('https://httpbin.org/get')
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
