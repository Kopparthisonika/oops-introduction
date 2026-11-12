# 1. Procedural Programming

def add(a, b):
    return a + b

print(add(10, 20))


# 2. Functional Programming

def square(x):
    return x * x

print(square(5))


# 3. Class

class Student:
    pass


# 4. Object

student1 = Student()


# 5. Properties / Attributes and Behaviors / Methods

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print("Student is studying")

    def write_exam(self):
        print("Student is writing an exam")

    def attend_class(self):
        print("Student is attending class")


# 6. Creating an Object and Accessing Properties

student1 = Student("Ravi", 20)

print(student1.name)
print(student1.age)

student1.study()
student1.write_exam()
student1.attend_class()