requests库提示警告：

    InsecureRequestWarning: Unverified HTTPS request is being made. 
    Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings InsecureRequestWarning)

1、Python3访问HTTPS时移除SSL认证：

    req = requests.get(url, verify=False)
    
2、但移除认证后控制台总是抛出警告：

    InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings InsecureRequestWarning)

3、根据提示路径https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings可找到方法一些解决办法，简单的办法可用移除警告：disable_warning
在请求之前添加如下代码即可。 

```python
import requests
requests.packages.urllib3.disable_warnings()
```