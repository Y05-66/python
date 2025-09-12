class Student:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def __str__(self):
        return "姓名：%s 年龄：%d 地址：%s" % (self.name, self.age, self.address)


student = []
total_students = 10
for i in range(total_students):
    print(f"当前添加第{i + 1}个学生信息，总共需要录入{total_students}个学生信息")
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    address = input("请输入学生地址：")
    student.append(Student(name, age, address))
    print(student[i])