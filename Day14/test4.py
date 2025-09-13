# filter() 函数的作用是从可迭代对象中筛选出符合条件的元素，返回一个迭代器

# 筛选出偶数
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = filter(lambda x: x % 2 == 0, number)
print(list(even))

# 筛选出大于5的数
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greater_than_5 = filter(lambda x: x > 5, number)
print(list(greater_than_5))
