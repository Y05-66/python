mytuple = ('周杰伦',11,['football','music'])

index = mytuple.index(11)
print(f"11在元组中的下标索引值是：{index}")

print(mytuple[0])

mytuple[2].remove('football')
print(mytuple)

mytuple[2].append('coding')
print(mytuple)