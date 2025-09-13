# map() 函数的作用是将一个函数应用于一个或多个可迭代对象（如列表、元组等）的每一个元素，并返回一个迭代器

# 对列表每个元素平方
def square(x):
    return x ** 2


number = [1, 2, 3, 4]
square = map(square, number)
print(list(square))
