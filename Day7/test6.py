try:
    f = open("D:/abc.txt","r",encoding="utf-8")
except Exception as e:
    print("出现异常了")
else:
    print("没有异常")
finally:
    f.close()