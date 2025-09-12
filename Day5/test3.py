def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数的类型为：{type(compute)}")
    print(f"计算结果为：{result}")


def compute(x, y):
    return x + y


test_func(compute)
