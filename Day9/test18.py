# 对形参进行类型注解
def add(a: int, b: int):
    return a + b


# 对返回值进行类型注解
def func(data: list) -> list:
    return data


func([1, 2, 3, 4, 5])
