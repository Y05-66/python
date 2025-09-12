import json
# 准备列表，列表内每一个元素都是字典，将其转换为JSON
data = [{"name":"张三","age":18},{"name":"李四","age":20},{"name":"王五","age":22}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 准备字典，将其转换为JSON
data = {"name":"张三","age":18}
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将JSON字符串转换为Python数据类型[{k:v,k:v}, {k:v,k:v}]
s = '[{"name":"张三","age":18},{"name":"李四","age":20},{"name":"王五","age":22}]'
l = json.loads(s)
print(type(l))
print(l)

# 将JSON字符串转换为Python数据类型{k:v,k:v}
s = '{"name":"张三","age":18}'
d = json.loads(s)
print(type(d))
print(d)