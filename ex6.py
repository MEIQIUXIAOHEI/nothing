# 定义类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"My name is {self.name}, and I am {self.age} years old."

# 继承示例
class CollegeStudent(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def info(self):
        return f"My name is {self.name}, and I study {self.major}."

# 使用
p1 = Person("Alice", 20)
p2 = CollegeStudent("Bob", 22, "Computer Science")

print(p1.info())   # My name is Alice, and I am 20 years old.
print(p2.info())   # My name is Bob, and I study Computer Science.
