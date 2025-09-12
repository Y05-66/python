import urllib.request
import random

proxies_pool = [
    {'http': '118.24.219.150.2563'},
    {'http': '119.3.226.131.2563'},
    {'http': '117.136.118.131.2563'},
]
proxies = random.choice(proxies_pool)
url = 'https://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 '
                  'Safari/537.36 Edg/136.0.0.0'
}
request = urllib.request.Request(url=url, headers=headers)
handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
html = response.read().decode('utf-8')
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(html)
