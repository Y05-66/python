# reduce()作用是将一个函数累积地应用于可迭代对象的所有元素，从左到右，最终将序列缩减为单个值
from functools import reduce

# 计算列表元素的乘积
number = [1, 2, 3, 4]
# 计算 ((((1*2)*3)*4)*5)
result = reduce(lambda x, y: x * y, number)
print(result)

# 计算列表元素之和
number = [1, 2, 3, 4]
add = reduce(lambda x, y: x + y, number)
print(add)

# 使用初始值
number = [1, 2, 3, 4]
add = reduce(lambda x, y: x + y, number, 10)
print(add)

# 找出最大值
number=[15,24,11,16]
max_num=reduce(lambda x,y:x if x>y else y,number)
print(max_num)
