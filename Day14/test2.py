# map() 函数的作用是将一个函数应用于一个或多个可迭代对象（如列表、元组等）的每一个元素，并返回一个迭代器

# 对列表每个元素平方
def square(x):
    return x ** 2


number = [1, 2, 3, 4]
square = map(square, number)
print(list(square))

# 使用 lambda 匿名函数

number = [1, 2, 3, 4]
square = map(lambda x: x ** 2, number)
print(list(square))

# 处理多个可迭代对象
number1 = [1, 2, 3, 4]
number2 = [5, 6, 7, 8]
add = map(lambda x, y: x + y, number1, number2)
print(list(add))

# 类型转换
str_num = ['1', '2', '3', '4']
int_num = map(int, str_num)
print(list(int_num))
