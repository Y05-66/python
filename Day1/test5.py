a = 10
if int(input("请输入第一次猜想的数字：")) == a:
    print("恭喜你，猜对了")
elif int(input("不对，再猜一次：")) == a:
    print("恭喜你，猜对了")
elif int(input("不对，再猜最一次：")) == a:
    print("恭喜你，猜对了")
else:
    print("Sorry,全部猜错了，我想的是:",a)
