my_str = "hello world"
value1 = my_str[1]
value2 = my_str[-10]
print(f"从字符串{my_str}取下标为2的值为：{value1}，取下标为-10的值为：{value2}")

# 字符串不可以修改

value = my_str.index("hello")
print(f"在字符串{my_str}中，hello的下标为：{value}")

new_my_str = my_str.replace("hello", "python")
print(f"将字符串{my_str}中的hello替换为python后的结果是：{new_my_str}")

my_str_list = my_str.split(" ")
print(f"将字符串{my_str}按空格进行切割后的结果是：{my_str_list}")

my_str = "  hello world  "
my_str = my_str.strip()
print(f"去除字符串{my_str}中的空格后的结果是：{my_str}")

my_str = "12hello world"
my_str = my_str.lstrip("12")
print(f"去除字符串{my_str}中的12后的结果是：{my_str}")

print(my_str.count('l'))

num = len(my_str)
print(f"字符串{my_str}的长度为：{num}")