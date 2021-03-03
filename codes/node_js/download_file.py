import requests

url = '''https://dynamic6.scrape.center/js/chunk-2f73b8f3.8f2fc3cd.js'''


resp = requests.get(url)

if resp and resp.status_code == 200:
    content = resp.content
    with open('chunk-2f73b8f3.8f2fc3cd.js', 'wb') as f:
        f.write(content)
