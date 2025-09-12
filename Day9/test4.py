class Student:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("初始化完成")


stu = Student("张三", 18, "123456789")
print(stu.name)
print(stu.age)
print(stu.tel)
