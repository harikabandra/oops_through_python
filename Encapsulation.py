class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # Private attribute

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

# Creating an instance of Student
student = Student("Harika", 95)

print("Student Name:", student.name)
print("Marks:", student.get_marks())

# Updating the private attribute using the setter method
student.set_marks(98)

print("Updated Marks:", student.get_marks())