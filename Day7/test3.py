try:
    # 1 / 0
    print(a)
except(ZeroDivisionError,NameError) as e:
    print("捕获到除数为0的异常或者变量名不存在的异常")