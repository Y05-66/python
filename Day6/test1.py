f = open("D:/测试.txt","r",encoding="UTF—8")

print(type(f))

# print(f"从文件中读取的数据为：{f.read()}")

lines = f.readlines()
print(type(lines))
print(lines)

for line in lines:
    print(line)

f.close()
f.sleep(500000)

with open("D:/测试.txt","r",encoding="UTF—8"):
    for line in f:
        print(line)