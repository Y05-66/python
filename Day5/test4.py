def test_add(compute):
    result = compute(1,2)
    print(f"结果为：{result}")

test_add(lambda x,y:x+y)