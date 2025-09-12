def outer(name):
    def inner(age):
        print(f"<{name}>{age}<{name}>")

    return inner


fun1 = outer("张三")
fun1(18)

fun2 = outer("李四")
fun2(20)
