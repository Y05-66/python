my_dict = {"周杰伦": 99, "林俊杰": 98, "张学友": 97}

# 添加键值对
my_dict["刘德华"] = 66
print(my_dict)

# 修改键值对
my_dict["周杰伦"] = 33
print(my_dict)

#  删除键值对
score = my_dict.pop("周杰伦")
print(score)

# 清空元素
my_dict.clear()
print(my_dict)

my_dict = {"周杰伦": 99, "林俊杰": 98, "张学友": 97}
# 获取全部的key
print(my_dict.keys())

# 遍历键值对
for key, value in my_dict.items():
    print(f"{key}的分数是：{value}")

# 统计字典内的元素数量
print(len(my_dict))
