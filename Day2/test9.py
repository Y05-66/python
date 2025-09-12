num = 100
count = 0
for x in range(1,num):
    if x % 2 == 0:
        count += 1
print(f"1到100(不包括100)一共有{count}个偶数")