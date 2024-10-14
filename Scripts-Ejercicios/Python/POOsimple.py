class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, career):
        super().__init__(name, age)
        self.career = career

def info(Student):
    print(f"Name: {Student.name}")
    print(f"Age: {Student.age}")
    print(f"Career: {Student.career}")

student = Student("Acxel", 21, "Software Engineering")
info(student)