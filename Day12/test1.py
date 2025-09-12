import urllib.request

# 定义一个访问地址的—url
url = 'http://www.baidu.com'

# 模拟浏览器向服务器发送请求 response响应
response = urllib.request.urlopen(url)
# read方法返回的是一个bytes字节流，需要解码成字符串
# decode解码
html = response.read().decode('utf-8')
print(html)