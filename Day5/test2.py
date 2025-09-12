def user_info(name, age, gender):
    print("姓名：%s, 年龄：%d, 性别：%s" % (name, age, gender))


user_info("小琪", 18, "女")

user_info(name="小琪", age=18, gender="女")
user_info(age=20, name="小王", gender="男")
user_info("婷婷", gender="女", age=18)


def user_info2(name, age, gender):
    print(f"姓名是：{name},年龄是：{age},性别是：{gender}")


user_info2("小琪", 18, "女")


def user_info3(*args):
    print(f"args参数的类型是：{type(args)}，内容是：{args}")


user_info3("小琪", 18, "女")


def user_info4(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)}，内容是：{kwargs}")


user_info4(name="小琪", age=18, gender="女")
