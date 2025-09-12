f1 = open("D:/test.txt","r",encoding="utf-8")
f2 = open("D:/bank.txt","w",encoding="utf-8")
for line in f1:
    f2.write(line)
f2.close()
f1.close()