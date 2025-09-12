import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# 一个类型和六个方法
# response是HTTPResponse类型
# print(type(response))

# 按照一个字节一个字节的去读
# content = response.read()
# print(content)

# 返回多少个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 读取所有行
# content = response.readlines()
# print(content)

# 获取状态码  200 表示成功
# print(response.getcode())

# 获取url
# print(response.geturl())

# 获取是一个状态信息
print(response.getheaders())