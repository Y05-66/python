my_set = {"小琪","小赵","小张","小琪","小赵","小张","小琪","小赵","小张"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("小王")
my_set.add("小琪")
print(f"my_set的内容是：{my_set}")

# 移除元素
my_set.remove("小王")
print(f"my_set的内容是：{my_set}")

# 随机取出一个元素
num = my_set.pop()
print(f"my_set的内容是：{my_set}，取出的元素是：{num}")

# 清空集合
my_set.clear()
print(f"my_set的内容是：{my_set}")

# 取2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"set1的内容是：{set1}，set2的内容是：{set2}，set3的内容是：{set3}")

# 消除2个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"set1的内容是：{set1}，set2的内容是：{set2}")

# 取2个集合的交集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.intersection(set2)
print(f"set1的内容是：{set1}，set2的内容是：{set2}，set3的内容是：{set3}")

# 取2个集合的并集
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"set1的内容是：{set1}，set2的内容是：{set2}，set3的内容是：{set3}")

# 统计集合元素的数量len()
set1 = {1,2,3,4,5}
print(f"set1的内容是：{set1}，set1的长度是：{len(set1)}")

# 集合的遍历
set1 = {1,2,3,4,5}
for i in set1:
    print(i)
