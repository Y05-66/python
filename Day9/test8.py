class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __le__(self,  other):
        return self.age <= other.age


stu1 = Student("小王", 18)
stu2 = Student("小琪", 19)
print(stu1 <= stu2)
print(stu2 <= stu1)