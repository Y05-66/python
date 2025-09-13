# sorted() 函数的作用是对可迭代对象进行排序，返回一个新的列表

# 对列表排序
number = [6, 2, 1, 4, 5, 0, 7, 8, 9]
sorted_number = sorted(number)
print(sorted_number)

# 对元组排序
number = (6, 2, 1, 4, 5, 0, 7, 8, 9)
sorted_number = sorted(number)
print(sorted_number)

# 对字符串排序
string = 'hello world'
sorted_string = sorted(string)
print(sorted_string)

# 对字典排序
dict = {'name': 'Tom', 'age': 18, 'sex': 'male'}
sorted_dict = sorted(dict.items())
print(sorted_dict)

# key 参数 忽略大小写
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
