f = open("D:/word.txt","r",encoding="utf-8")
test = f.read()
count = 0
for line in test:
    if line == "a":
        count += 1
print(count)
f.close()