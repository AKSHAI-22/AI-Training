class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)

class Student(Person):
    def study(self):
        print(self.name,"is studying")

class Teacher(Person):
    def teach(self):
        print(self.name,"is teaching")

student=Student("Akshai",18)
teacher=Teacher("Arun",30)

student.display()
student.study()

teacher.display()
teacher.teach()