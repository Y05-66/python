# 定义单个元素的元素
t4 = ("hello",)
print(f"t4的类型是：{type(t4)},t4的内容是：{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")

# 下标索引去取出内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

# 元组的操作：index查找方法
t6 = ("小琪","小王", "小张")
index = t6.index("小琪")
print(f"小琪在列表中的索引值是：{index}")

# 元组的操作：count统计方法
t7 = ("小王","小王","小王","小琪","小琪")
num = t7.count("小琪")
print(f"在元组中，小琪出现的次数是：{num}")

# 元组的操作：len函数统计元组元素的数量
t8 = ("小王","小王","小王","小琪","小琪")
num = len(t8)
print(f"元组t8中元素的数量是：{num}")

# 元组的遍历：while
index = 0
while index < len(t8):
    print(f"元组的元素是：{t8[index]}")
    index += 1
    
# 元组的遍历：for
for element in t8:
    print(f"元组中的元素是：{element}")