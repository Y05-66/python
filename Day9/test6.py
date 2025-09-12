class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "姓名：%s，年龄：%s" % (self.name, self.age)


stu = Student("小明", 18)
print(stu)
print(str(stu))
