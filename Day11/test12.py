import re
s = "永远相信美好的事情即将发生"
# match方法从头匹配
result = re.match("永远", s)
print(result)
# print(result.group())
# print(result.span())

# search方法从 anywhere 匹配
result = re.search("美好的", s)
print(result)

# findall搜索全部匹配
result = re.findall("美好", s)
print(result)