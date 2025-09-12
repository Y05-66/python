import re

# 匹配账号，只能由字母和数字组成，长度限制6到10位
r = "^[a-zA-Z0-9]{6,10}$"
s = "abc123"
result = re.match(r, s)
print(result)

# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
r = "^[1-9][0-9]{4,10}$"
s = "123456789"
result = re.match(r, s)
print(result)

# 匹配邮箱地址，只允许QQ，163，gmail这三种邮箱地址
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'a.b.c.d.e.f@qq.com.a'
result = re.match(r, s)
print(result)
