class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


stu1 = Student("小明",18)
stu2 = Student("小王",18)
print(stu1 == stu2)