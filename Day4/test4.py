mylist = [21,25,21,23,22,20]

mylist.append(31)
print(mylist)

mylist2 = [29,33,30]
mylist.extend(mylist2)
print(mylist)

print(mylist[0])
print(mylist[-1])

index = mylist.index(31)
print(f"31在列表中的下标索引值是：{index}")