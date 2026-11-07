class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Name:",self.name)
        print("Age:",self.age)

sam1 = Student("Harika", 19)
sam1.info()

sam2 = Student("Karthika", 18)
sam2.info()