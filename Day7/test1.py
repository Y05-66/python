try:
    f = open("D:/abc.txt","r",encoding="utf-8")
except:
    print("文件不存在")
    f = open("D:/abc.txt","w",encoding="utf-8")