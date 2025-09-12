import urllib.request
import urllib.parse

url = 'https://cn.bing.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6'

# 请求对象的定制为了解决反爬的第一种手段
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 '
                  'Safari/537.36 Edg/136.0.0.0'
}

# 将周杰伦三个字变成unicode编码的格式
# 需要使用urllib.parse.quote()函数
name = urllib.parse.quote('周杰伦')
url = url + name

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的内容
content = response.read().decode('utf-8')

print(content)
