class Student:

    def __init__(self):
        self.name = "Harika"
        self._branch = "AIML"
        self.__marks = 98

    def display_public(self):
        print("Public Name:", self.name)

    def _display_protected(self):
        print("Protected Branch:", self._branch)

    def __display_private(self):
        print("Private Marks:", self.__marks)

    def display_all(self):
        self.display_public()
        self._display_protected()
        self.__display_private()


student = Student()

print("Name:", student.name)
print("Branch:", student._branch)

student.display_all()