import urllib.request
import urllib.parse
import json
url = 'https://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 '
                  'Safari/537.36 Edg/136.0.0.0'
}
data = {
    'kw': 'cute'
}
# post请求的参数必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
# post的请求的参数，是不会拼接在url的后面的，而是需要放在请求对象定制的参数中
requests = urllib.request.Request(url=url, data=data, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(requests)
content = response.read().decode('utf-8')

# 字符串转换为json对象
obj = json.loads(content)
print(obj)
