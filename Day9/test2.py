class Student:
    name = None

    def say1(self):
        print("我叫%s" % self.name)

    def say2(self, mag):
        print("我叫%s,%s" % (self.name, mag))


stu = Student()

stu.name = "张三"
stu.say1()
stu.say2("今天天气不错")
