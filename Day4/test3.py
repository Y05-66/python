mylist = ["小琪","小王","小赵"]
# 查找某元素在列表内的下标索引

index = mylist.index("小琪")
print(f"小琪在列表中的下标索引值是：{index}")

# 如果查找的元素不存在，会报错
# index = mylist.index("小张")
# print(f"小张在列表中的下标索引值是：{index}")

# 修改特定下标索引的值
mylist[0] = "宁姚"
print(mylist)

# 在特定位置插入新元素
mylist.insert(1,"小晓")
print(mylist)

# 在列表尾部追加‘单个’新元素
mylist.append("小孙")
print(mylist)

# 在列表尾部追加‘多个’新元素
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(mylist)

# 删除指定下标索引的元素(两种方式)
mylist3 = [1,2,3,4,5]
# 方式1：del 列表[下标]
del mylist3[0]
print(mylist3)
# 方式2：列表.pop(下标)
mylist4 = [1,2,3,4,5]
mylist4.pop(0)
print(mylist4)

# 删除某元素在列表中的第一个匹配值
mylist5 = [1,2,3,4,5,1,2,3,4,5]
mylist5.remove(1)
print(mylist5)

# 清空列表
mylist6 = [1,2,3,4,5]
mylist6.clear()
print(mylist6)

# 统计列表内某元素的数量
mylist7 = [1,2,3,4,5,1,2,3,4,5]
print(mylist7.count(1))

# 统计列表中全部的元素数量
print(len(mylist7))

