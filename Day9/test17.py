# 基础数据类型注解
import json
import random

var_1: int = 10
var_2: float = 10.0
var_3: str = "hello world"
var_4: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"name": "张三", "age": 18}
# 容器类型详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, str, float] = (1, "hello", 10.0)
my_dict: dict[str, int] = {"name": 18, "age": 18}

# 在注解中进行类型注解
var_1 = random.randint(1, 10)  # type:int
var_2 = json.load('{"name":"zhnagsan"}')  #  type:dict


def func():
    return 10


var_3 = func()  #  type:int
