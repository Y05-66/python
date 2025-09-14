# 匿名函数

L = list(filter(lambda x: x % 2 == 0, range(1, 20)))
print(L)


# 装饰器

def my_decorator(func):  # func就是要包装的礼物
    print("开始包装礼物了")

    def wrapper():  # 这就是包装好的礼物盒
        print("🎀 打开礼物盒")  # 包装纸的功能
        func()  # 里面的实际礼物
        print("🎀 关上礼物盒")  # 包装纸的功能

    return wrapper  # 返回包装好的礼物盒


# 2. 定义一个"礼物"（原始函数）
def say_hello():
    print("Hello,我是礼物")


# 3. 手动包装礼物（这就是@装饰器的本质）
say_hello = my_decorator(say_hello)
# 4. 打开礼物盒
say_hello()


# 语法糖
def my_decorator(func):
    def wrapper():
        print("🎀 打开礼物盒")
        func()
        print("🎀 关上礼物盒")

    return wrapper


# 使用@语法糖自动包装
@my_decorator
def say_hello():
    print("Hello,我是礼物")


# 直接使用包装好的函数
say_hello()


# @my_decorator等价与
# def say_hello():
#     print("Hello,我是礼物")
# say_hello = my_decorator(say_hello)


def my_decorator(func):
    print("⚠️ 注意：装饰器现在执行！")  # 这行在导入时就执行

    def wrapper():
        print("包装功能")
        func()

    return wrapper


@my_decorator  # 这里就会执行my_decorator函数！
def say_hello():
    print("Hello")


print("准备调用函数...")
say_hello()  # 这里才执行wrapper函数
